
CREATE OR REPLACE FUNCTION public.reporte_especifico(
	trabajador text,
	inicio date,
	finalizar date)
RETURNS json
    LANGUAGE 'plpgsql'
    COST 100.0

AS $function$

declare 
 data_ json;
 info json;
 total text;
begin
	total:=(select to_char(sum(case when pl.hora is not null and pl.precio is not null then (pl.precio*pl.hora) else 0 end), 'FM$999,999,999,990') as total_horas
				 from auth_user as u
				 inner join usuario_empleado as e on (u.id=e.usuario_ptr_id and u.id=any(trabajador::int[]))
				 left join operacion_labor as l on 
                        (u.id=l.empleado_id and l.cerrado=true and 
                          cast(l.ini as date) >= inicio and cast(l.ini as date) <= finalizar 
                         and cast(l.fin as date) >= inicio and cast(l.fin as date) <= finalizar)
				 left join operacion_pagolabor as pl on (l.id=pl.labor_id and 
                          cast(pl.ini as date) >= inicio and cast(pl.ini as date) <= finalizar 
                         and cast(pl.fin as date) >= inicio and cast(pl.fin as date) <= finalizar) );

	data_:= (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
			select l.ini,l.fin,
			       to_char(sum(case when pl.hora is not null then pl.hora else 0 end),'999,9999D99') as horas,
			       sum(case when pl.hora is not null and pl.precio is not null then (pl.precio*pl.hora) else 0 end) as total ,
			       to_char(sum(case when pl.hora is not null and pl.precio is not null then (pl.precio*pl.hora) else 0 end), 'FM$999,999,999,990') as total_horas
				 from auth_user as u
				 inner join usuario_empleado as e on (u.id=e.usuario_ptr_id and u.id=any(trabajador::int[]))
				 left join operacion_labor as l on (u.id=l.empleado_id and l.cerrado=true and 
                          cast(l.ini as date) >= inicio and cast(l.ini as date) <= finalizar 
                         and cast(l.fin as date) >= inicio and cast(l.fin as date) <= finalizar)
				 left join operacion_pagolabor as pl on (l.id=pl.labor_id and
                          cast(pl.ini as date) >= inicio and cast(pl.ini as date) <= finalizar 
                         and cast(pl.fin as date) >= inicio and cast(pl.fin as date) <= finalizar) group by l.id,l.ini,l.fin
	) p);
	info:=(SELECT COALESCE(array_to_json(array_agg(row_to_json(p2))), '[]') from (
		select e.direccion,a.first_name as nombre,a.last_name as apellidos,u.identificacion,u.telefono_celular as celular, t.nombre as tienda,c.nombre as ciudad,em.first_name as empresa from usuario_empleado as e 
		  inner join auth_user as a on (e.usuario_ptr_id=a.id)
		  inner join usuario_usuario as u on (u.user_ptr_id=e.usuario_ptr_id and  u.user_ptr_id=any(trabajador::int[]))
		  inner join empresa_tienda as t on (t.id=e.tienda_id)
		  inner join empresa_ciudad  as c on (c.id=t.ciudad_id)
		  inner join auth_user as em on (em.id = t.empresa_id) limit 1
	) p2);
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		select data_,info,case when length(total) = 0 then '$ 0' else total end as ttotal
	) p); 
end;

$function$;

ALTER FUNCTION public.reporte_especifico(text, date, date)
    OWNER TO postgres;