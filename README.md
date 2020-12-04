# Twitter_and_Locations_gis



## **Explain project**  
  
**This Project included two project with two app seperated in django rest framework is for crawler twitter and location finder with postgis that we send polyegone points to query and query get records that  inside its polygon**  
  
**Architecture**  
I used of Design Patterns  **Strategy and Repository And Factory**  
  
**Repository** for data maybe in future we want using of postgres or any database  
  
**Strategy** for management Behavior of app maybe in future we want that will create new Behavior  for my app.  
  
**factory** for management create of app maybe in future we want that will create new object or class for my app.  

## **How to using of url Api?**  
  
First you must going to url **api/menu**  
  
**API's Are** :  
  
**api/twitter/online-tweets-save** 

**method is POST and have 3 parameter : username, start_date , end_date**

date format is : 2020-11-02


**api/twitter/save-images: method is POST and have 2 parameter : key , value for get from db**

**api/twitter/read-all: method is GET have not parameter**

**api/twitter/find-data:  method is POST and have 2 parameter : key , value for get from db**

**api/location/all-locations-find:  method is GET**
