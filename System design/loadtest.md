# Load Test - bulk upload API 

```
**`env`**` ``-`` pixelbinz0`
**`server`**` ``-`` hidan panel server`
**`api`**` ``-`` https``:``//api.pixelbinz0.de/service/panel/misc/v2.0/org/9003/skus/bulk-upload`
**`current scaling`**` ``-`` 
    Pnl:
    Scale:
        Min: 2
        Desired: 2
        Max: 2`
**`current memory `****`and`****` CPU`**` ``-`` `
`    ``Pnl``:`
    `    ``Resources``:`
    `        requests``:`
        `        cpu``:`` ``500m`
        `        memory``:`` ``500Mi`
    `        limits``:`
        `        cpu``:`` ``1000m`
        `        memory``:`` ``1000Mi`
```




#### **Load test result (using k6 grafana)**

* maximum virtual users - 200 
* batch size - 50 (sku data)

[Image: Screenshot 2025-01-24 at 3.23.21 PM.png]
### **Load Test Summary** 

#### **1️⃣ General Metrics**

* **Total Requests (http_reqs)**: **9,641**
* **Total Iterations**: **9,641** (Each Virtual User (VU) completed one request per iteration)
* **Peak Virtual Users (vus_max)**: **200**
* **Requests per Second (RPS)**: **24.65 req/sec**
* **Total Data Sent**: **111 MB (~285 kB/s)**
* **Total Data Received**: **3.0 MB (~7.8 kB/s)**

* * *

#### **2️⃣ Request Duration Analysis**

* **Average Response Time**: **2.81s** (🚨 This is quite slow!)
* **Median (p50)**: **2.58s**
* **90th Percentile (p90)**: **5.73s** (10% of requests took longer than this)
* **95th Percentile (p95)**: **6.36s**
* **Max Response Time**: **9.41s** (🚨 Some requests are taking **way too long!**)


* * *

#### **3️⃣ Request Failure Analysis**

* **Failed Requests (http_req_failed)**: **0.07% (7 out of 9,641)** ✅
* **Success Rate**: **99.93%** (which is good)


Newrelic transaction link -  [](https://onenr.io/0VjY8v1YER0)https://onenr.io/0PwJ9v16BQ7

Grafana link - https://grafana-m1.core.pixelbinz0.de/d/_E5zJOqGz/kubernetes-deployment?orgId=1&from=1737711780000&to=1737712559000&var-Deployment=pixb-hidan-pnl-srvr-dply&var-Node=All

CPU usage : 
[Image: Screenshot 2025-01-24 at 3.28.30 PM.png]Memory Usage : 
[Image: Screenshot 2025-01-24 at 3.28.59 PM.png]

 
