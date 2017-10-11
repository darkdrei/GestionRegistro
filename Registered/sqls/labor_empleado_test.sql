-- FUNCTION: public.labor_empleado_test(integer)

-- DROP FUNCTION public.labor_empleado_test(integer);

CREATE OR REPLACE FUNCTION public.labor_empleado_test(
  id_labor integer)
RETURNS boolean
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
    switch_dia boolean :=false;
    freno_labor boolean := false;
begin
  raise notice 'eso es lo q hay';
    RAISE NOTICE 'Done refreshing materialized views.';
    for temporal in select l.id,(EXTRACT(EPOCH FROM l.fin)-EXTRACT(EPOCH FROM l.ini))/3600.0 as tiempo,
                 l.ini,l.fin,t.empresa_id as empresa,
                           l.empleado_id as empleado,t.ciudad_id as ciudad 
                           from operacion_labor as l 
                            inner join usuario_empleado as e on(l.id=id_labor and l.empleado_id=e.usuario_ptr_id)
                            inner join auth_user as u on (u.id=e.usuario_ptr_id)
                            inner join empresa_tienda as t on (e.tienda_id=t.id) limit 1
    loop
      fecha_inicio :=temporal.ini;
        fecha_fin :=temporal.fin;
        tiempo_total:=temporal.tiempo; 
        tiempo:=0;
        freno_labor:=false;
        switch_dia :=false;
        raise notice '--------------------------------  % ',temporal.tiempo;
        raise notice '% -- % -- %',temporal.ini,temporal.fin,temporal.tiempo;
      <<loop_extraer_valor>>
        loop
             select c.id as id_lab,
                      c.valor,
                      c.inicio,
                      c.fin,c."ciudad_id" as ciudad,
                      c."empresa_id" as empresa,
                      ds.valor as dia_semana
                      from usuario_empleado as e 
          inner join empresa_tienda as t on (t.id=e.tienda_id and e.usuario_ptr_id=18)                     
                      inner join operacion_configuracion as c on (t.ciudad_id=c.ciudad_id and t.empresa_id=c.empresa_id)
                      inner join operacion_configuracion_dias as cd on (cd.configuracion_id=c.id and c.estado=true)
                      inner join operacion_diasemana as ds on (cd.diasemana_id=ds.id)
                      where temporal.empresa= c."empresa_id" and temporal.ciudad=c."ciudad_id" and
                    ds.valor = case when EXTRACT(DOW FROM fecha_inicio)= 0 then 7 else (EXTRACT(DOW FROM fecha_inicio)) end and
                        cast(fecha_inicio as time) >= cast(c.inicio as time) and cast(c.fin as time) >= cast(fecha_inicio as time)
                      order by c.empresa_id,c."ciudad_id", ds.valor,c.inicio asc into dia;
              raise notice 'respuesta intervalo %  --> % -- %',dia,fecha_inicio,fecha_fin;
              if dia is not null then 
                        raise notice 'el dia no es nulo---> % ++ % ',fecha_fin,dia.fin;
                        raise notice 'valores para los tiemos %  % %',cast(fecha_fin as time),cast(fecha_inicio as time),(cast(fecha_fin as time) < cast(fecha_inicio as time)) ;
                        if cast(fecha_fin as time) < cast(fecha_inicio as time) then
                            switch_dia:=true;
                        else
                            switch_dia:=false;
                        end if;
                        raise notice 'esta es la respuesta --> % ',switch_dia;
                  if (cast(fecha_fin as time) >= cast(dia.fin as time)) or  switch_dia =true then
                          raise notice 'entro en 1';
        tiempo:= (EXTRACT(EPOCH FROM dia.fin)-EXTRACT(EPOCH FROM cast(fecha_inicio as time)))/3600.0;
      else
              raise notice 'entro en 2';
              freno_labor:=true;
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
              exit loop_extraer_valor when freno_labor;
      end loop;
    end loop;          
    return true;
end;

$function$;

ALTER FUNCTION public.labor_empleado_test(integer)
    OWNER TO postgres;
