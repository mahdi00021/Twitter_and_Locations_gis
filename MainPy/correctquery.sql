SELECT locations.name_city,
       locations.latitude,
       locations.longitude
FROM   locations
WHERE  ST_Contains(
         ST_SetSRID(
           'POLYGON((-15.0292969 47.6357836,-15.2050781 47.5172007,-16.2597656 29.3821751,35.0683594 26.1159859,38.0566406 47.6357836,-15.0292969 47.6357836))'::GEOMETRY,
           4326
         ),
         locations.the_geom
       )