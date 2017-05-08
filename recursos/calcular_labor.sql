select * from operacion_labor;

select time '16:00:00' - time '05:00:00';

select * from operacion_labor as l
inner join usuario_empleado as e on(l.empleado_id=e.usuario_ptr_id)
inner join auth_user as u on (u.id=e.usuario_ptr_id)
inner join empresa_tienda as t on (e.tienda_id=t.id)
select time '15:00:00'

select (EXTRACT(EPOCH FROM l.fin)-EXTRACT(EPOCH FROM l.ini))/3600.0 as tiempo,l.ini,l.fin,t.empresa_id as empresa,l.empleado_id as empleado,t.ciudad_id from operacion_labor as l
inner join usuario_empleado as e on(l.empleado_id=e.usuario_ptr_id)
inner join auth_user as u on (u.id=e.usuario_ptr_id)
inner join empresa_tienda as t on (e.tienda_id=t.id)

select * from empresa_ciudad
select * from empresa_empresa
select * from operacion_configuracion order by empresa_id, cuidad_id,valor
insert into operacion_configuracion(valor,inicio,fin,estado,ciudad_id,empresa_id) select valor,inicio,fin,estado,2,empresa_id from operacion_configuracion

select * from operacion_configuracion limit 5 offset 2

select *  from operacion_configuracion as c
		 inner join operacion_configuracion_dias as cd on (cd.configuracion_id=c.id and c.estado=true)
         inner join operacion_diasemana as ds on (cd.diasemana_id=ds.id)
         order by c.empresa_id,c."ciudad_id", ds.valor,c.inicio asc

select c.id as id_lab,c.valor,c.inicio,c.fin,c."ciudad_id" as ciudad,c."empresa_id" as empresa,cd.diasemana_id as dia_semana  from operacion_configuracion as c
		 inner join operacion_configuracion_dias as cd on (cd.configuracion_id=c.id and c.estado=true)
         inner join operacion_diasemana as ds on (cd.diasemana_id=ds.id)
         order by c.empresa_id,c."ciudad_id", cd.diasemana_id,c.inicio asc

insert into operacion_configuracion_dias(configuracion_id,diasemana_id) select configuracion_id+6,diasemana_id from operacion_configuracion_dias

select ini

select ini, EXTRACT(dow  from ini) from operacion_labor
drop function get_labores()
select get_labores()

create or replace function get_labores() returns int as $$
declare
	temporal record;
    dia record;
    temporal_inicio time;
    temporal_fin time;
    temporal_dia integer;
    bandera boolean :=false;
    fecha_inicio TIMESTAMP;
    fecha_fin TIMESTAMP;
    tiempo_total double precision :=0;
    tiempo double precision :=0;
    con integer:=0;
begin
	raise notice 'eso es lo q hay';
    RAISE NOTICE 'Done refreshing materialized views.';
    <<stop>>
    for temporal in select (EXTRACT(EPOCH FROM l.fin)-EXTRACT(EPOCH FROM l.ini))/3600.0 as tiempo,l.ini,l.fin,t.empresa_id as empresa,l.empleado_id as empleado,t.ciudad_id as ciudad from operacion_labor as l
                            inner join usuario_empleado as e on(l.empleado_id=e.usuario_ptr_id)
                            inner join auth_user as u on (u.id=e.usuario_ptr_id)
                            inner join empresa_tienda as t on (e.tienda_id=t.id)
    loop
    	fecha_inicio :=temporal.ini;
        fecha_fin :=temporal.fin;
        tiempo_total:=temporal.tiempo;
        tiempo:=0;
        raise notice '--------------------------------';
        raise notice '% -- % -- %',temporal.ini,temporal.fin,temporal.tiempo;
    	<<loop_extraer_valor>>
        loop
        	   select c.id as id_lab,
                      c.valor,
                      c.inicio,
                      c.fin,c."ciudad_id" as ciudad,
                      c."empresa_id" as empresa,
                      ds.valor as dia_semana
                      from operacion_configuracion as c
                      inner join operacion_configuracion_dias as cd on (cd.configuracion_id=c.id and c.estado=true)
                      inner join operacion_diasemana as ds on (cd.diasemana_id=ds.id)
                      where temporal.empresa= c."empresa_id" and temporal.ciudad=c."ciudad_id" and
                		ds.valor = case when EXTRACT(DOW FROM fecha_inicio)= 0 then 7 else (EXTRACT(DOW FROM fecha_inicio)) end and
                        cast(fecha_inicio as time) >= cast(c.inicio as time) and cast(c.fin as time) >= cast(fecha_inicio as time)
                      order by c.empresa_id,c."ciudad_id", ds.valor,c.inicio asc into dia;
              raise notice 'respuesta intervalo %  --> % -- %',dia,fecha_inicio,fecha_fin;
              if dia is not null then
              		if cast(fecha_fin as time) > cast(dia.fin as time) then
                     	tiempo:= (EXTRACT(EPOCH FROM dia.fin)-EXTRACT(EPOCH FROM cast(fecha_inicio as time)))/3600.0;
                    else
                    	tiempo:= (EXTRACT(EPOCH FROM fecha_fin)-EXTRACT(EPOCH FROM cast(fecha_inicio as time)))/3600.0;
                   	end if;
                    raise notice ' este es el tiempo %',tiempo;
                    fecha_inicio:= cast(fecha_inicio as timestamp) + cast(tiempo||' hour' as interval)+ time '00:00:01';
              end if;
              con:=con+1;
              raise notice '% - %',fecha_inicio,fecha_fin;
              raise notice '***************';
              exit loop_extraer_valor when dia is null;
              exit stop when con=10;
    	end loop;
    end loop;

    return 1;
end;
$$language plpgsql;
