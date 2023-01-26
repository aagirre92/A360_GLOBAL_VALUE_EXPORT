# INTRODUCTION
This script allows to programmatically create Global Values in a A360 Control Room, given a Global Value csv file**
# CONSIDERATIONS
Only tested for the following Global Value types:
* STRING
* NUMBER
# CSV template format
**Template must be in the following format**

|name                              |type  |description                                                                                           |value                                                                                               |isOverridable|
|----------------------------------|------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------|
|numCVRBotSpecialDelay             |NUMBER|This is the number of seconds bot will wait for window in CVR bot for downloading excel reports in SAP|180                                                                                                 |TRUE         |
|strConnectionString               |STRING|This is the connection string used for connecting to excel as database                                |Provider=Microsoft.ACE.OLEDB.12.0;Data Source=FileName;Extended Properties="Excel 12.0 Xml;HDR=YES";|TRUE         |
|strSAPApplicationPath             |STRING|This is the SAP installation path used to launch/open SAP desktop application                         |C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe                                             |TRUE         |
|strSharedDrivePath                |STRING|This is the shared drive path used for logs, screenshots, etc                                         |Z:\DEV\OTC                                                                                          |TRUE         |
|testGlobalChangeable              |STRING|                                                                                                      |global value, can be changed                                                                        |TRUE         |
|cr_environment                    |STRING|                                                                                                      |dev                                                                                                 |FALSE        |

# USAGE (powershell)
```
.\main.py --cr_url="https://aa1-app2019.iacc.epam.com" --username="andoni_aguirre_aranguren" --api_key="1234jlfs" --gv_csv_path="C:\Us
ers\Andoni_Aguirre_Arang\Downloads\global_values.csv"

```

# FUTURE POSSIBLE ENHANCEMENTS
* Multi-threading for the http requests
