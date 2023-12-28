[comment]: # "Auto-generated SOAR connector documentation"
# MongoDB

Publisher: Splunk  
Connector Version: 2.0.9  
Product Vendor: MongoDB  
Product Name: MongoDB  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 5.1.0  

This app supports CRUD operations in a MongoDB database

[comment]: # "    File: README.md"
[comment]: # "    Copyright (c) 2018-2023 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
This app will ignore the HTTP_PROXY and HTTPS_PROXY environment variables, as it does not use HTTP
to connect to the database.

### On Creating New Databases and Collections

When creating a new asset, you must specify something for the **database** parameter, which will be
the name of the database. If you specify one which does not currently exist, then the app will carry
on as normal (though there will be a warning in the test connectivity modal). After running a **post
data** action, then that database will be created. Similarly, by specifying a **collection** which
does not currently exist as a parameter to **post data** , you can create new collections.

  

### BSON Strings

Many parameters in this app, like **data** and **filter** expect a deserializable BSON string. In
respects to this app, BSON is a superset of JSON, so any valid JSON will be properly deserialized.
However, BSON can also deserialize many other types. For example, MongoDB uses an ObjectID type by
default for the "\_id" field. In order to use this, like to create a filter, the BSON string will
look like `     {"_id": {"$oid":"5a345190f059c57581d754f0"}}    ` . If you can install the
appropriate python modules (i.e. pymongo) then you can serialize python dictionaries to the
appropriate string in your playbook code. If that approach isn't possible, the result data from
**get data** will contain the appropriate representations, as well, which can be used as reference
for future actions.

## PyMongo

This app uses the PyMongo module, written by Bernie Hackett and is licensed under the Apache
Software License, Version 2.0, Copyright (2021) The Apache Software Foundation
(http://www.apache.org/).


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a MongoDB asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**host** |  required  | string | Host, Including Port Number
**database** |  required  | string | Database
**username** |  optional  | string | Username
**password** |  optional  | password | Password
**auth_fields** |  optional  | string | JSON String for Other Authentication Fields

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[post data](#action-post-data) - Add data to the database  
[get data](#action-get-data) - Get data from the database  
[update data](#action-update-data) - Update documents which match a given filter  
[delete data](#action-delete-data) - Delete documents which match a given filter  
[list tables](#action-list-tables) - List all the collections in the database  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'post data'
Add data to the database

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**collection** |  required  | Collection | string |  `mongodb collection` 
**data** |  required  | Data to add, as a JSON string | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success 
action_result.parameter.collection | string |  `mongodb collection`  |   collection3 
action_result.parameter.data | string |  |   {"column1": "value1", "column2": "value2", "_id": 1}  [{"col1": "val1"}, {"col1": "val1"}]  {"column1": "value1", "column2": "value2"} 
action_result.data.\*._id | numeric |  |   1 
action_result.data.\*._id.$oid | string |  |   5a345b47f059c578423564b4 
action_result.summary | string |  |  
action_result.message | string |  |   Successfully added to database 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'get data'
Get data from the database

Type: **investigate**  
Read only: **True**

By leaving the <b>filter</b> parameter blank, all documents in the collection will be returned.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**collection** |  required  | Collection | string |  `mongodb collection` 
**filter** |  optional  | Filter for documents | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success 
action_result.parameter.collection | string |  `mongodb collection`  |   collection3 
action_result.parameter.filter | string |  |   {"_id": {"$oid": "5a345b47f059c578423564b4"}} 
action_result.data.\*._id | string |  |   1 
action_result.data.\*._id.$oid | string |  |   5a345b47f059c578423564b4 
action_result.summary | string |  |  
action_result.message | string |  |   Successfully got data 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'update data'
Update documents which match a given filter

Type: **generic**  
Read only: **False**

All documents which match the <b>filter</b> parameter will be updated.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**collection** |  required  | Collection | string |  `mongodb collection` 
**filter** |  required  | Update all documents matching this filter | string | 
**update** |  required  | The updates to apply | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success 
action_result.parameter.collection | string |  `mongodb collection`  |   collection3 
action_result.parameter.filter | string |  |   {"_id": {"$oid":"5a345190f059c57581d754f0"}} 
action_result.parameter.update | string |  |   {"$set": {"column1": "updated value 1 (again)"}} 
action_result.summary.modified_count | numeric |  |   1 
action_result.message | string |  |   Successfully updated data 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'delete data'
Delete documents which match a given filter

Type: **generic**  
Read only: **False**

All documents which match the <b>filter</b> parameter will be deleted.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**collection** |  required  | Collection | string |  `mongodb collection` 
**filter** |  required  | Delete all documents matching this filter | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success 
action_result.parameter.collection | string |  `mongodb collection`  |   collection3 
action_result.parameter.filter | string |  |   {"_id": {"$oid":"5a345b47f059c578423564b4"}} 
action_result.summary.deleted_count | numeric |  |   1 
action_result.message | string |  |   Successfully deleted data 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'list tables'
List all the collections in the database

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success 
action_result.data.\*.collection | string |  `mongodb collection`  |   testcollect 
action_result.summary | string |  |  
action_result.message | string |  |   Successfully listed collections 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 