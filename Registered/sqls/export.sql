select * from operacion_labor

select * from (select u.identificacion,a.first_name,a.last_name,l.id,l.ini,l.fin,round((EXTRACT(EPOCH FROM l.fin-l.ini)/3600)::numeric,2) from motorizado_infomoto as info 
         inner join usuario_usuario as u on (info.empleado_id = u.user_ptr_id)
         inner join auth_user as a on (a.id=u.user_ptr_id)
         left join operacion_labor as l on (l.empleado_id=a.id)) as t 
         
COPY public.registro_subcuenta TO '/home/csv/labores_final.csv' DELIMITER ',' CSV HEADER;


select * from operacion_labor where id in (5,4,7,13,29)
update operacion_labor set fin = cast('2017-09-09 20:30:00' as timestamp) where id = 5;
update operacion_labor set fin = cast('2017-09-09 21:30:00' as timestamp) where id = 4;
update operacion_labor set fin = cast('2017-09-11 21:00:00' as timestamp) where id = 7;
update operacion_labor set fin = cast('2017-09-14 21:00:00' as timestamp) where id = 13;
update operacion_labor set fin = cast('2017-09-23 22:00:00' as timestamp) where id = 29;
select get_labores()
select * from operacion_pagolabor
delete from operacion_pagolabor
select * from (select u.identificacion,a.first_name,a.last_name,l.id,l.ini,l.fin,round((EXTRACT(EPOCH FROM l.fin-l.ini)/3600)::numeric,2) as final from motorizado_infomoto as info 
         inner join usuario_usuario as u on (info.empleado_id = u.user_ptr_id)
         inner join auth_user as a on (a.id=u.user_ptr_id)
         left join operacion_labor as l on (l.empleado_id=a.id)) as t order by t.identificacion asc ,t.final desc
         
COPY (
select * from (select u.identificacion,a.first_name,a.last_name,l.id,l.ini,l.fin,round((EXTRACT(EPOCH FROM l.fin-l.ini)/3600)::numeric,2) as final from motorizado_infomoto as info 
         inner join usuario_usuario as u on (info.empleado_id = u.user_ptr_id)
         inner join auth_user as a on (a.id=u.user_ptr_id)
         left join operacion_labor as l on (l.empleado_id=a.id)) as t order by t.identificacion asc ,t.final desc
) TO '/home/csv/labores_fina.csv' DELIMITER ',' CSV HEADER;