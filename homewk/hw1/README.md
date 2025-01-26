#Q1
code: docker run -it python:3.12.8 bash
      pip --version
answer:24.3.1

#Q2
answer:db:5433

#Q3
code:
      select count(*)
      from green_tripdata
      where trip_distance <= 1
      ----
      select count(*)
      from green_tripdata
      where trip_distance > 1 and trip_distance <= 3
      ----
      select count(*)
      from green_tripdata
      where trip_distance > 3 and trip_distance <= 7
      ----
      select count(*)
      from green_tripdata
      where trip_distance > 7 and trip_distance <= 10
      ----
      select count(*)
      from green_tripdata
      where trip_distance > 10

answer:104,838; 199,013; 109,645; 27,688; 35,202


#Q4
code:
      select extract(day from lpep_pickup_datetime) as day, max(trip_distance)
      from green_tripdata
      group by day
      order by 2 desc
answer:2019-10-31

#Q5
code:
      select 
            extract(day from lpep_pickup_datetime) as day,
            sum(total_amount),
      CONCAT(zp."Borough", ' | ', zp."Zone") "pickup_loc"
      from green_tripdata g
      join zones zd
      on g."DOLocationID" = zd."LocationID"
      join zones zp
      on g."PULocationID" = zp."LocationID"
      where extract(day from lpep_pickup_datetime) = 18
      group by day,"pickup_loc"
      having sum(total_amount) >13000
answer:East Harlem North, East Harlem South, Morningside Heights

#Q6
code:
      select 
            CONCAT(zp."Borough", ' | ', zp."Zone") AS "pickup_loc",
      CONCAT(zd."Borough", ' | ', zd."Zone") AS "dropoff_loc",
      max(tip_amount) AS max_tip
      from green_tripdata g
      join zones zd ON g."DOLocationID" = zd."LocationID"
      join zones zp ON g."PULocationID" = zp."LocationID"
      where zp."Zone" = 'East Harlem North'
      group by "pickup_loc","dropoff_loc"
      order by max_tip DESC
      limit 1
answer:FK Airport

#Q7
answer:
terraform init, terraform apply -auto-approve, terraform destroy




