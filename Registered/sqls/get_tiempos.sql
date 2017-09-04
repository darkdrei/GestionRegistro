-- Function: get_tiempo(timestamp without time zone, interval)

-- DROP FUNCTION get_tiempo(timestamp without time zone, interval);

CREATE OR REPLACE FUNCTION get_tiempo(
    tiempo timestamp without time zone,
    horas interval)
  RETURNS timestamp without time zone AS
$BODY$
begin
	return (tiempo + horas +  time '00:00:01');
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION get_tiempo(timestamp without time zone, interval)
  OWNER TO postgres;
