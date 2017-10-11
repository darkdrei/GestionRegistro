
CREATE OR REPLACE FUNCTION public.get_total_trabajador2(
	id_supervisor integer,
	busqueda text,
	empresa integer,
	tienda integer,
	ciudad integer,
	inicio date,
	finalizar date)
RETURNS json
    LANGUAGE 'plpgsql'
    COST 100.0

AS $function$

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
	       round(sum(case when pl.hora is not null and pl.precio is not null then pl.hora else 0 end)::numeric,1) as total_turnos,
	       sum(case when pl.hora is not null and pl.precio is not null then (pl.precio*pl.hora) else 0 end) as total ,
	       to_char(sum(case when pl.hora is not null and pl.precio is not null then (pl.precio*pl.hora) else 0 end), 'FM$999,999,999,990') as total_horas
		 from auth_user as u
		 inner join usuario_empleado as e on (u.id=e.usuario_ptr_id)
		 inner join usuario_usuario as usu on (usu.user_ptr_id=u.id)
		 inner join motorizado_infomoto as im on (u.id=im.empleado_id and im.estado=true)
		 inner JOIN empresa_tienda as t ON 
		                        (
		                           t.id = e.tienda_id 
		                           and 
		                           ((tienda=0 and t.id != 0) or (tienda != 0 and t.id=tienda))
		                           and 
		                           (
					       (empresa != 0 and t.empresa_id=empresa) 
					     or 
					        (
					           empresa=0 and  t.empresa_id in (select super_emp.empresa_id from empresa_supervisor_empresas as super_emp where super_emp.supervisor_id=id_supervisor)
					        )
					  )
				       )
		 inner join empresa_ciudad as c on (t.ciudad_id=c.id and (
					(ciudad != 0 and t.ciudad_id=ciudad) or (ciudad=0 and  t.ciudad_id in (select super_emp.ciudad_id from empresa_supervisor_ciudad as super_emp where super_emp.supervisor_id=id_supervisor))))
		 inner join auth_user as em on (em.id=t.empresa_id)
		 left join operacion_labor as l on (u.id=l.empleado_id and l.cerrado=true and l.fin>=inicio and l.fin <=finalizar)
		 left join operacion_pagolabor as pl on (l.id=pl.labor_id) group by u.id, usu.identificacion, u.first_name,u.last_name,t.nombre,em.first_name,c.nombre
	) p);
end;

$function$;

ALTER FUNCTION public.get_total_trabajador2(integer, text, integer, integer, integer, date, date)
    OWNER TO postgres;
