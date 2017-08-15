-- Function: get_total_trabajador(integer, text, integer, integer, integer, date, date)

-- DROP FUNCTION get_total_trabajador(integer, text, integer, integer, integer, date, date);

CREATE OR REPLACE FUNCTION get_total_trabajador(
    id_supervisor integer,
    busqueda text,
    empresa integer,
    tienda integer,
    ciudad integer,
    inicio date,
    finalizar date)
  RETURNS json AS
$BODY$
begin
	return (SELECT COALESCE(array_to_json(array_agg(row_to_json(p))), '[]') from (

        SELECT e.usuario_ptr_id AS id_empleado,
            u.identificacion,
            auth.first_name AS nom_emp,
            auth.last_name AS ape_emp,
            t.nombre AS nom_tienda,
            emp.first_name as nom_empre,
            sum(case when lc.labor_id is not null then 1 else 0 end) as total_turnos,
            sum(case when lc.hora is not null then lc.hora else 0 end) as total_horas,
            sum(case when lc.hora is not null and lc.precio is not null then (lc.hora*lc.precio) else 0 end) as total_horas
           FROM usuario_empleado e
             JOIN usuario_usuario u ON (e.usuario_ptr_id = u.user_ptr_id AND u.estado = true and e.tienda_id in (select tem_tienda.id from empresa_supervisor_empresas as tem_emp inner join empresa_tienda as tem_tienda on (tem_emp.empresa_id=tem_tienda.empresa_id and tem_emp.supervisor_id=id_supervisor)))
             JOIN auth_user auth ON (auth.id = u.user_ptr_id)
             JOIN empresa_tienda t ON (t.id = e.tienda_id and
                  (
                      (tienda=0 and t.id in (select tem_tienda.id from empresa_supervisor_empresas as tem_emp inner join empresa_tienda as tem_tienda on (tem_emp.empresa_id=tem_tienda.empresa_id and tem_emp.supervisor_id=id_supervisor)))
                      or
                      (tienda !=0 and t.id=tienda)
                  ))
        	 JOIN empresa_ciudad as c on (c.id=t.ciudad_id and
                 (ciudad=0 and c.id in (select distinct(tem_ciudad.id) from empresa_supervisor_empresas as tem_emp
inner join empresa_tienda as tem_tienda on (tem_emp.empresa_id=tem_tienda.empresa_id)
inner join empresa_ciudad as tem_ciudad on (tem_tienda.ciudad_id=tem_ciudad.id and tem_ciudad.status=true and tem_emp.supervisor_id=id_supervisor) order by tem_ciudad.id asc))
                 or
                 (ciudad !=0 and c.id=ciudad))
             JOIN auth_user as emp ON (t.empresa_id = emp.id and (
                 (empresa=0 and emp.id in (select tem_emp.empresa_id from empresa_supervisor_empresas as tem_emp where tem_emp.supervisor_id=id_supervisor))
                 or
                 (empresa!=0 and emp.id=empresa)
             ))
             LEFT JOIN operacion_labor l ON (auth.id = l.empleado_id and cast(l.fin as date)>=inicio and cast(l.fin as date)<=finalizar)
             LEFT JOIN operacion_pagolabor lc ON (l.id = lc.labor_id AND l.estado = true)
             group by e.usuario_ptr_id,u.identificacion, auth.first_name, auth.last_name,emp.id,emp.first_name,t.nombre,lc.labor_id
	) p);
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION get_total_trabajador(integer, text, integer, integer, integer, date, date)
  OWNER TO postgres;
