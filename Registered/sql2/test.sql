select t2.ini,t2.fin,to_char(t2.total_horas,'FM$999,999,999,990') as total_horas,trunc(t2.horas)||' horas y '||trunc((trunc(t2.horas, 2)-trunc(t2.horas))*60)||' minutos.' as horas from(select t1.orden, (select min(bus.ini) from operacion_labor as bus where extract(day from bus.ini)=t1.orden and  bus.empleado_id=t1.empleado) as ini,(select max(bus.fin) from operacion_labor as bus where extract(day from bus.ini)=t1.orden and  bus.empleado_id=t1.empleado) as fin,sum(case when t1.total is not null then t1.total else 0 end) as total_horas,sum(case when t1.horas is not null then cast(t1.horas as numeric) else 0 end) as horas,t1.empleado 
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
				 inner join usuario_empleado as e on (u.id=e.usuario_ptr_id and u.id=any('{4}'::int[]))
				 left join operacion_labor as l on (u.id=l.empleado_id and l.cerrado=true and 
                          cast(l.ini as date) >= '26/09/2017'::date and cast(l.ini as date) <= '11/10/2017'::date 
                         and cast(l.fin as date) >= '26/09/2017'::date and cast(l.fin as date) <= '11/10/2017'::date ) 
             group by l.id,l.ini,l.fin,u.id) as tf order by tf.ini asc,tf.id) as t1 group by t1.orden,t1.empleado) as t2 order by t2.ini