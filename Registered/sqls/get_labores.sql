-- FUNCTION: public.get_labores()

-- DROP FUNCTION public.get_labores();

CREATE OR REPLACE FUNCTION public.get_labores(
	)
    RETURNS integer
    LANGUAGE 'plpgsql'
    COST 100.0

AS $function$
 
declare 
  temporal record;
    dia record;
    temporal_inicio time;
    temporal_fin time;
    temporal_dia integer;
    bandera boolean :=false;
    fecha_inicio TIMESTAMP;
    fecha_fin TIMESTAMP;
    tem text;
    tiempo_total double precision :=0;
    tiempo double precision :=0;
    con integer:=0;
begin
  raise notice 'eso es lo q hay';
    RAISE NOTICE 'Done refreshing materialized views.';
    for temporal in select l.id,(EXTRACT(EPOCH FROM l.fin)-EXTRACT(EPOCH FROM l.ini))/3600.0 as tiempo,
                 l.ini,l.fin,t.empresa_id as empresa,
                           l.empleado_id as empleado,t.ciudad_id as ciudad 
                           from operacion_labor as l 
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
                      tiempo:= (EXTRACT(EPOCH FROM cast(fecha_fin as time))-EXTRACT(EPOCH FROM cast(fecha_inicio as time)))/3600.0;
                    end if;
                    tem :=''||fecha_inicio;
                    fecha_inicio:= cast(fecha_inicio as timestamp) + cast(tiempo||' hour' as interval)+ time '00:00:01';
                    if tiempo >0 then
                      insert into operacion_pagolabor (ini,fin,precio,hora,labor_id)
                                    values(tem,fecha_inicio,dia.valor,tiempo,temporal.id);
                    end if;
              end if;
              con:=con+1;
              raise notice 'tiempo % -- % - %',tiempo,fecha_inicio,fecha_fin;
              raise notice '***************';
              exit loop_extraer_valor when dia is null;
              exit loop_extraer_valor when tiempo <=0;
      end loop;
    end loop;
                            
    return 1;
end;

$function$;

ALTER FUNCTION public.get_labores()
    OWNER TO postgres;
