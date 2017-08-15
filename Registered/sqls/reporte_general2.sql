-- Function: reporte_general(text, date, date)

-- DROP FUNCTION reporte_general(text, date, date);

CREATE OR REPLACE FUNCTION reporte_general(
    trabajador text,
    inicio date,
    finalizar date)
  RETURNS json AS
$BODY$
begin
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select
		   u.id AS id_empleado,
		   u.first_name AS nom_emp,
		   u.last_name AS ape_emp,
		   usu.identificacion,
		   t.nombre AS nom_tienda,
		   em.first_name as nom_empre,
		   c.nombre,
	       sum(case when pl.hora is not null and pl.precio is not null then 1 else 0 end) as total_turnos,
	       sum(case when pl.hora is not null and pl.precio is not null then (pl.precio*pl.hora) else 0 end) as total ,
	       to_char(sum(case when pl.hora is not null and pl.precio is not null then (pl.precio*pl.hora) else 0 end), 'FM$999,999,999,990') as total_horas
		 from auth_user as u
		 inner join usuario_empleado as e on (u.id=e.usuario_ptr_id and u.id=any(trabajador::int[]))
		 inner join usuario_usuario as usu on (usu.user_ptr_id=u.id)
		 inner JOIN empresa_tienda as t ON (t.id = e.tienda_id)
		 inner join empresa_ciudad as c on (t.ciudad_id=c.id)
		 inner join auth_user as em on (em.id=t.empresa_id)
		 left join operacion_labor as l on (u.id=l.empleado_id and l.cerrado=true and l.fin>=inicio and l.fin <=finalizar)
		 left join operacion_pagolabor as pl on (l.id=pl.labor_id) group by u.id, usu.identificacion, u.first_name,u.last_name,t.nombre,em.first_name,c.nombre
	) p);
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION reporte_general(text, date, date)
  OWNER TO postgres;
