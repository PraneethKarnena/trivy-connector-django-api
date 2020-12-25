
# Trivy Connector - Django API

* This is a connector for Trivy as Django API
* This project runs Trivy commands in the **background**, **asynchronously**, so that user does not have to wait until the scan in finished
* Two simple endpoints are provided for requesting a scan and viewing the result

## Components

* Python 3
* Django 2.2 LTS
* PostgreSQL 12
* Celery 5

## Setup

* Install dependencies: `pip install -r requirements.txt`
* Move `rivy_connector_django_api/.env.example` to `rivy_connector_django_api/.env` and add corresponding values
* Create database tables: `python manage.py migrate`
* Run server: `python manage.py runserver`

## Usage

* Request a Scan:
	* Request
				```
				POST  /api/scan/
				{
				"target": "nginx"
				}
			```
	
	* Response
		```
		{  "id":  "6aa301e5-b3d5-4818-b8a4-0d820f04441b",  "created_at":  "2020-12-25T19:11:39.128140Z",  "updated_at":  "2020-12-25T19:11:39.128219Z",  "target":  "nginx",  "result":  null,  "status":  "PEN",  "has_error":  false,  "error_message":  null  }
		```

* Scan Result:
	* Request
		```GET  /api/result/6aa301e5-b3d5-4818-b8a4-0d820f04441b/```

	* Response
		```
		{
	    "id": "6aa301e5-b3d5-4818-b8a4-0d820f04441b",
	    "created_at": "2020-12-25T19:11:39.128140Z",
	    "updated_at": "2020-12-25T19:11:44.295597Z",
	    "target": "nginx",
	    "result": [
	        {
	            "Type": "debian",
	            "Target": "nginx (debian 10.7)",
	            "Vulnerabilities": [
	                {
	                    "CVSS": {
	                        "nvd": {
	                            "V2Score": 4.3,
	                            "V3Score": 3.7,
	                            "V2Vector": "AV:N/AC:M/Au:N/C:N/I:P/A:N",
	                            "V3Vector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N"
	                        }
	                    },
	                    "Layer": {
	                        "DiffID": "sha256:87c8a1d8f54f3aa4e05569e8919397b65056aa71cdf48b7f061432c98475eee9",
	                        "Digest": "sha256:6ec7b7d162b24bd6df88abde89ceb6d7bbc2be927f025c9dd061af2b0c328cfe"
	                    },
	                    "CweIDs": [
	                        "CWE-347"
	                    ],
	                    "PkgName": "apt",
	                    "Severity": "LOW",
	                    "PrimaryURL": "https://avd.aquasec.com/nvd/cve-2011-3374",
	                    "References": [
	                        "https://access.redhat.com/security/cve/cve-2011-3374",
	                        "https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=642480",
	                        "https://people.canonical.com/~ubuntu-security/cve/2011/CVE-2011-3374.html",
	                        "https://security-tracker.debian.org/tracker/CVE-2011-3374",
	                        "https://snyk.io/vuln/SNYK-LINUX-APT-116518"
	                    ],
	                    "Description": "It was found that apt-key in apt, all versions, do not correctly validate gpg keys with the master keyring, leading to a potential man-in-the-middle attack.",
	                    "PublishedDate": "2019-11-26T00:15:00Z",
	                    "SeveritySource": "debian",
	                    "VulnerabilityID": "CVE-2011-3374",
	                    "InstalledVersion": "1.8.2.2",
	                    "LastModifiedDate": "2019-12-04T15:35:00Z"
	                }
	            ]
	        }
	    ]
		}
		```


## Screenshots

* Scan

![Scan](https://i.ibb.co/CPr2Scf/trivy-connector-scan-request.png)


* Result

![Result](https://i.ibb.co/CPr2Scf/trivy-connector-scan-request.png)