create or replace function get_total_trabajador(busqueda text,empresa text,tienda text,ciudad text, ini date,fin date) returns json as $$
begin
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (

        SELECT e.usuario_ptr_id AS id_empleado,
            u.identificacion,
            auth.first_name AS nom_emp,
            auth.last_name AS ape_emp,
            t.nombre AS nom_tienda,
            emp.first_name as nom_emp,
            sum(case when lc.labor_id is not null then 1 else 0 end) as total_turnos,
            sum(case when lc.hora is not null then lc.hora else 0 end) as total_horas,
            sum(case when lc.hora is not null and lc.precio is not null then (lc.hora*lc.precio) else 0 end) as total_horas
           FROM usuario_empleado e
             JOIN usuario_usuario u ON (e.usuario_ptr_id = u.user_ptr_id AND u.estado = true)
             JOIN auth_user auth ON (auth.id = u.user_ptr_id)
             JOIN empresa_tienda t ON (t.id = e.tienda_id and t.id=any(tienda::int[]))
             JOIN auth_user as emp ON (t.empresa_id = emp.id and emp.id=any(empresa::int[]))
             LEFT JOIN operacion_labor l ON (auth.id = l.empleado_id)
             LEFT JOIN operacion_pagolabor lc ON (l.id = lc.labor_id AND l.estado = true)
             group by e.usuario_ptr_id,u.identificacion, auth.first_name, auth.last_name,emp.id,emp.first_name,t.nombre,lc.labor_id
	) p);
end;
$$language plpgsql;

/*******************************************************************************/
-- FUNCTION: public.tabla_items(integer, text, integer, integer, integer)

-- DROP FUNCTION public.tabla_items(integer, text, integer, integer, integer);

CREATE OR REPLACE FUNCTION public.tabla_items(
	id_des integer,
	search_ text,
	order_ integer,
	start_ integer,
	length_ integer)
RETURNS text
    LANGUAGE 'plpgsql'
    COST 100.0

AS $function$

declare
	l json;
	t integer;
	id_emp integer :=0;
begin
	select empresa_id from domicilios_empleado where usuario_ptr_id = 14 limit 1 into id_emp;
	if id_emp is null then
		id_emp=0;
	end if;
	select count(id) from domicilios_items where "empresaI_id"=id_emp into t;
	SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (
		 select codigo,initcap(descripcion),initcap(presentacion),id from domicilios_items where "empresaI_id"=id_emp and
		 codigo like '%'||search_||'%' or descripcion like '%'||search_||'%' or presentacion like '%'||search_||'%' limit length_ offset start_
	) p into l;
	return '{"recordsFiltered": '|| t ||', "recordsTotal": '|| t ||', "data": '|| l||'}';
end;

$function$;

ALTER FUNCTION public.tabla_items(integer, text, integer, integer, integer)
    OWNER TO postgres;

select lb.nom_emp as nombre,lb.ape_emp as apellidos from usuario_empleado as e
  left join operacion_labor as l on(e.usuario_ptr_id=l.empleado_id and l.estado=true)
  left join labores as lb on(lb.labor_id=l.id)  group by e.usuario_ptr_id,lb.nom_emp,lb.ape_emp

  select * from usuario_empleado as e
  left join operacion_labor as l on(e.usuario_ptr_id=l.empleado_id and l.estado=true)
  left join labores as lb on(lb.labor_id=l.id)

  select * from labores

SELECT e.usuario_ptr_id AS id_empleado,
    u.identificacion,
    auth.first_name AS nom_emp,
    auth.last_name AS ape_emp,
    t.nombre AS nom_tienda,
    emp.first_name as nom_emp,
    sum(case when lc.labor_id is not null then 1 else 0 end) as total_turnos,
    sum(case when lc.hora is not null then lc.hora else 0 end) as total_horas,
    sum(case when lc.hora is not null and lc.precio is not null then (lc.hora*lc.precio) else 0 end) as total_horas
   FROM usuario_empleado e
     JOIN usuario_usuario u ON (e.usuario_ptr_id = u.user_ptr_id AND u.estado = true)
     JOIN auth_user auth ON (auth.id = u.user_ptr_id)
     JOIN empresa_tienda t ON (t.id = e.tienda_id)
     JOIN auth_user emp ON (t.empresa_id = emp.id)
     LEFT JOIN operacion_labor l ON (auth.id = l.empleado_id)
     LEFT JOIN operacion_pagolabor lc ON (l.id = lc.labor_id AND l.estado = true)
     group by e.usuario_ptr_id,u.identificacion, auth.first_name, auth.last_name,emp.id,emp.first_name,t.nombre,lc.labor_id

SELECT * FROM usuario_empleado e
     JOIN usuario_usuario u ON (e.usuario_ptr_id = u.user_ptr_id AND u.estado = true)
     JOIN auth_user auth ON (auth.id = u.user_ptr_id)
     JOIN empresa_tienda t ON (t.id = e.tienda_id)
     JOIN auth_user emp ON (t.empresa_id = emp.id)
     LEFT JOIN operacion_labor l ON (auth.id = l.empleado_id)
     LEFT JOIN operacion_pagolabor lc ON (l.id = lc.labor_id AND l.estado = true)
     group by e.usuario_ptr_id,u.identificacion, auth.first_name, auth.last_name,emp.id,emp.first_name,t.nombre,lc.labor_id


select * from empresa_empresa where user_ptr_id=any('{23,24}'::int[])

create or replace function get_total_trabajador(busqueda text,empresa text,tienda text,ciudad text, ini date,fin date) returns json as $$
begin
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (

        SELECT e.usuario_ptr_id AS id_empleado,
            u.identificacion,
            auth.first_name AS nom_emp,
            auth.last_name AS ape_emp,
            t.nombre AS nom_tienda,
            emp.first_name as nom_emp,
            sum(case when lc.labor_id is not null then 1 else 0 end) as total_turnos,
            sum(case when lc.hora is not null then lc.hora else 0 end) as total_horas,
            sum(case when lc.hora is not null and lc.precio is not null then (lc.hora*lc.precio) else 0 end) as total_horas
           FROM usuario_empleado e
             JOIN usuario_usuario u ON (e.usuario_ptr_id = u.user_ptr_id AND u.estado = true)
             JOIN auth_user auth ON (auth.id = u.user_ptr_id)
             JOIN empresa_tienda t ON (t.id = e.tienda_id and t.id=any(tienda::int[]))
             JOIN auth_user as emp ON (t.empresa_id = emp.id and emp.id=any(empresa::int[]))
             LEFT JOIN operacion_labor l ON (auth.id = l.empleado_id)
             LEFT JOIN operacion_pagolabor lc ON (l.id = lc.labor_id AND l.estado = true)
             group by e.usuario_ptr_id,u.identificacion, auth.first_name, auth.last_name,emp.id,emp.first_name,t.nombre,lc.labor_id
	) p);
end;
$$language plpgsql;
