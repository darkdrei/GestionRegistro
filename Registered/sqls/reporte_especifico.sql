
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
			select t2.ini,t2.fin,to_char(t2.total_horas,'FM$999,999,999,990') as total_horas,trunc(t2.horas)||' horas y '||trunc((trunc(t2.horas, 2)-trunc(t2.horas))*60)||' minutos.' as horas from(
    select t1.orden, (
                      select min(bus.ini) from operacion_labor as bus where extract(day from bus.ini)=t1.orden and  bus.empleado_id=t1.empleado) as ini,
                      (select max(bus.fin) from operacion_labor as bus where extract(day from bus.ini)=t1.orden and bus.estado=true and  bus.empleado_id=t1.empleado) as fin,sum(case when t1.total is not null then t1.total else 0 end) as total_horas,sum(case when t1.horas is not null then cast(t1.horas as numeric) else 0 end) as horas,t1.empleado 
         from(select EXTRACT(DAY FROM tf.ini) as orden,tf.horas,tf.total,tf.total_horas,tf.id as empleado  from(select u.id,l.ini,l.fin,
			       sum(case when (select count(pl.id) from operacion_pagolabor as pl  where pl.labor_id=l.id limit 1) > 0 then 
                                     (select sum(case when pl.precio is not null and pl.hora is not null then pl.hora else 0 end) from operacion_pagolabor as pl where pl.labor_id=l.id) 
                                    else 0 end) as horas,
			       sum(case when (select count(pl.id) from operacion_pagolabor as pl  where pl.labor_id=l.id limit 1) > 0 then 
                                     (select sum(case when pl.precio is not null and pl.hora is not null then pl.precio*pl.hora else 0 end) from operacion_pagolabor as pl where pl.labor_id=l.id) 
                                    else 0 end) as total ,
			       to_char(sum(case when (select count(pl.id) from operacion_pagolabor as pl  where pl.labor_id=l.id limit 1) > 0 then 
                                     (select sum(case when pl.precio is not null and pl.hora is not null then pl.precio*pl.hora else 0 end) from operacion_pagolabor as pl where pl.labor_id=l.id) 
                                    else 0 end), 'FM$999,999,999,990') as total_horas
				 from auth_user as u
				 inner join usuario_empleado as e on (u.id=e.usuario_ptr_id and u.id=any(trabajador::int[]))
				 left join operacion_labor as l on (u.id=l.empleado_id and l.cerrado=true and 
                          cast(l.ini as date) >= inicio and cast(l.ini as date) <= finalizar 
                         and cast(l.fin as date) >= inicio and cast(l.fin as date) <= finalizar) 
             group by l.id,l.ini,l.fin,u.id) as tf order by tf.ini asc,tf.id) as t1 group by t1.orden,t1.empleado) as t2 order by t2.ini      
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
