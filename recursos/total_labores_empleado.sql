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
