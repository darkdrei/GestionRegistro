-- FUNCTION: public.get_tiempo(timestamp without time zone, interval)

-- DROP FUNCTION public.get_tiempo(timestamp without time zone, interval);

CREATE OR REPLACE FUNCTION public.get_tiempo(
	tiempo timestamp without time zone,
	horas interval)
RETURNS timestamp without time zone
    LANGUAGE 'plpgsql'
    COST 100.0

AS $function$

begin
	return (tiempo + horas +  time '00:00:01');
end;

$function$;

ALTER FUNCTION public.get_tiempo(timestamp without time zone, interval)
    OWNER TO postgres;
