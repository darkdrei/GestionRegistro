-- Function: reporte_especifico(text, date, date)

-- DROP FUNCTION reporte_especifico(text, date, date);

CREATE OR REPLACE FUNCTION reporte_especifico(
    trabajador text,
    inicio date,
    finalizar date)
  RETURNS json AS
$BODY$
begin
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select l.ini,l.fin,
	       to_char(sum(case when pl.hora is not null then pl.hora else 0 end),'999,9999D99') as horas,
	       sum(case when pl.hora is not null and pl.precio is not null then (pl.precio*pl.hora) else 0 end) as total ,
	       to_char(sum(case when pl.hora is not null and pl.precio is not null then (pl.precio*pl.hora) else 0 end), 'FM$999,999,999,990') as total_horas
		 from auth_user as u
		 inner join usuario_empleado as e on (u.id=e.usuario_ptr_id and u.id=any(trabajador::int[]))
		 left join operacion_labor as l on (u.id=l.empleado_id and l.cerrado=true)
		 left join operacion_pagolabor as pl on (l.id=pl.labor_id) group by l.id,l.ini,l.fin
	) p);
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION reporte_especifico(text, date, date)
  OWNER TO postgres;
