# PRODUCTION connection strings - EXT db
from pymongo import MongoClient,ASCENDING,DESCENDING, errors


DB_CONNECTION_URLS_OLD = {
    "rblfurniture" : "mongodb://fynd_rblfurniture_ext_readwrite:readWrite_rblfurniture_ext!2023@10.159.48.9:27017,10.159.48.11:27017,10.159.48.10:27017/rblfurniture_ext?replicaSet=re_extension_set&readPreference=secondaryPreferred",
    "logicerp" : "mongodb://logic_erp_ext_write:njdngWV0rq@10.159.48.9:27017,10.159.48.11:27017,10.159.48.10:27017/logic_erp_ext?replicaSet=re_extension_set&readPreference=secondaryPreferred",
    "vinculum" : "mongodb://fynd_vinculum_ext_readwrite:readWrite_vinculum_ext_fynd!2021@10.155.48.35:27017,10.155.48.36:27017/vinculum_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
    "easyecom" : "mongodb://fynd_easyecom_ext_readwrite:readWrite_easyecom_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/easyecom_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
    "increff" : "mongodb://fynd_increff_ext_readwrite:readWrite_increff_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/increff_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
    "omsguru": "mongodb://fynd_omsguru_ext_readwrite:readWrite_omsguru_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/omsguru_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
    "eshop": "mongodb://fynd_eshop_ext_readwrite:readWrite_eshop_ext!2023@10.155.48.35:27017,10.155.48.36:27017/eshop_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
    "fynd_konnect" : "mongodb://fynd_fynd_konnect_ext_readwrite:readWrite_fynd_konnect_ext!2023@10.155.48.35:27017,10.155.48.36:27017/fynd_konnect_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
    "browntape": "mongodb://fynd_browntape_ext_readwrite:readWrite_browntape_ext_fynd!2021@10.155.48.35:27017,10.155.48.36:27017/browntape_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
    "fyndpos": "mongodb://fynd_fyndpos_ext_readwrite:readWrite_fyndpos_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/fyndpos_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred"
}


DB_CONNECTION_URLS = {
    "ext" : {
        # "logicerp" : "mongodb://fynd_logic_erp_ext_readwrite:readWrite_logic_erp_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/logic_erp_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "vinculum" : "mongodb://fynd_vinculum_ext_readwrite:readWrite_vinculum_ext_fynd!2021@10.155.48.35:27017,10.155.48.36:27017/vinculum_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "easyecom" : "mongodb://fynd_easyecom_ext_readwrite:readWrite_easyecom_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/easyecom_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "increff" : "mongodb://fynd_increff_ext_readwrite:readWrite_increff_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/increff_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "omsguru": "mongodb://fynd_omsguru_ext_readwrite:readWrite_omsguru_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/omsguru_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "eshop": "mongodb://fynd_eshop_ext_readwrite:readWrite_eshop_ext!2023@10.155.48.35:27017,10.155.48.36:27017/eshop_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "fynd_konnect" : "mongodb://fynd_fynd_konnect_ext_readwrite:readWrite_fynd_konnect_ext!2023@10.155.48.35:27017,10.155.48.36:27017/fynd_konnect_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "browntape": "mongodb://fynd_browntape_ext_readwrite:readWrite_browntape_ext_fynd!2021@10.155.48.35:27017,10.155.48.36:27017/browntape_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "fyndpos": "mongodb://fynd_fyndpos_ext_readwrite:readWrite_fyndpos_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/fyndpos_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "rblfurniture" : "mongodb://rblfurniture_ext_write:sYjb9DNXjq@10.155.48.36:27017,10.155.48.35:27017/rblfurniture_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
         "rbl_tibco": "mongodb://fynd_rbl_tibco_ext_readwrite:readWrite_rbl_tibco_ext!2023@10.155.48.7:27017,10.155.48.35:27017,10.155.48.36:27017/rbl_tibco_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "clarksstore": "mongodb://fynd_clarksstore_ext_readwrite:readWrite_clarksstore_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/clarksstore_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "clarksware" : "mongodb://fynd_clarksware_ext_readwrite:readWrite_clarksware_ext_fynd!2022@10.155.48.35:27017,10.155.48.36:27017/clarksware_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "rbposdta" : "mongodb://fynd_rbposdta_ext_readwrite:readWrite_rbposdta_ext!2023@10.155.48.7:27017,10.155.48.35:27017,10.155.48.36:27017/rbposdta_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "rbl_tibco": "mongodb://fynd_rbl_tibco_ext_readwrite:readWrite_rbl_tibco_ext!2023@10.155.48.7:27017,10.155.48.35:27017,10.155.48.36:27017/rbl_tibco_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "rblsap" : "mongodb://rblsap_ext_write:Xwc9IVGaQn@10.155.48.35:27017,10.155.48.36:27017/rblsap_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "wizapp": "mongodb://wizapp_ext_write:KKDX3aorA7@10.155.48.35:27017,10.155.48.36:27017/wizapp_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "wondersoft" : "mongodb://fynd_wondersoft_ext_readwrite:readWrite_wondersoft_ext!2024@10.155.48.7:27017,10.155.48.35:27017,10.155.48.36:27017/wondersoft_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "jiopos" : "mongodb://jiopos_ext_write:Z5JForloK2@10.155.48.36:27017,10.155.48.35:27017/jiopos_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "jiopos_hamleys" : "mongodb://jiopos_hamleys_ext_write:li9F5yVHxo@10.155.48.36:27017,10.155.48.35:27017/jiopos_hamleys_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred",
        "jiopos_openapi": "mongodb://jiopos_openapi_ext_write:oE!IBlGKm5@10.155.48.35:27017,10.155.48.36:27017/jiopos_openapi_ext?replicaSet=re_extensions_set&readPreference=secondaryPreferred"

    },

    "inv": {},
    
   "logs": {
        # "rblfurniture":"mongodb://fynd_rblfurniture_logs_readwrite:readWrite_rblfurniture_logs!2024@10.155.48.136:27017,10.155.48.119:27017/rblfurniture_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "rbl_tibco":"mongodb://fynd_rbl_tibco_logs_readwrite:readWrite_rbl_tibco_logs!2024@10.155.48.136:27017,10.155.48.119:27017/rbl_tibco_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "rbposdta":"mongodb://fynd_rbposdta_logs_readwrite:readWrite_rbposdta_logs!2024@10.155.48.136:27017,10.155.48.119:27017/rbposdta_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "rblsap":"mongodb://fynd_rblsap_logs_readwrite:readWrite_rblsap_logs!2024@10.155.48.136:27017,10.155.48.119:27017/rblsap_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "clarksstore":"mongodb://fynd_clarksstore_logs_readwrite:readWrite_clarksstore_logs_fynd!2022@10.155.48.136:27017,10.155.48.119:27017/clarksstore_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "clarksware":"mongodb://fynd_clarksware_logs_readwrite:readWrite_clarksware_logs_fynd!2022@10.155.48.136:27017,10.155.48.119:27017/clarksware_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "wizapp":"mongodb://fynd_wizapp_logs_readwrite:readWrite_wizapp_logs!2024@10.155.48.136:27017,10.155.48.119:27017/wizapp_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "wondersoft":"mongodb://fynd_wondersoft_logs_readwrite:readWrite_wondersoft_logs!2024@10.155.48.136:27017,10.155.48.119:27017/wondersoft_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "jiopos":"mongodb://fynd_jiopos_logs_readwrite:readWrite_jiopos_logs!2024@10.155.48.136:27017,10.155.48.119:27017/jiopos_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "jiopos_hamleys": "mongodb://fynd_jiopos_hamleys_logs_readwrite:readWrite_jiopos_hamleys_logs!2024@10.155.48.136:27017,10.155.48.119:27017/jiopos_hamleys_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "jiopos_openapi":"mongodb://fynd_jiopos_openapi_logs_readwrite:readWrite_jiopos_openapi_logs!2024@10.155.48.136:27017,10.155.48.119:27017/jiopos_openapi_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        "vinculum":"mongodb://fynd_vinculum_logs_readwrite:readWrite_vinculum_logs_fynd!2021@10.155.48.136:27017,10.155.48.119:27017/vinculum_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "easyecom":"mongodb://fynd_easyecom_logs_readwrite:readWrite_easyecom_logs_fynd!2022@10.155.48.136:27017,10.155.48.119:27017/easyecom_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "increff":"mongodb://fynd_increff_logs_readwrite:readWrite_increff_logs!2024@10.155.48.136:27017,10.155.48.119:27017/increff_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        "omsguru":"mongodb://fynd_omsguru_logs_readwrite:readWrite_omsguru_logs_fynd!2022@10.155.48.136:27017,10.155.48.119:27017/omsguru_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "eshop":"mongodb://fynd_eshop_logs_readwrite:readWrite_eshop_logs!2024@10.155.48.136:27017,10.155.48.119:27017/eshop_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "fynd_konnect":"mongodb://fynd_fynd_konnect_logs_readwrite:readWrite_fynd_konnect_logs!2024@10.155.48.136:27017,10.155.48.119:27017/fynd_konnect_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "browntape":"mongodb://fynd_browntape_logs_readwrite:readWrite_browntape_logs_fynd!2021@10.155.48.136:27017,10.155.48.119:27017/browntape_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
        # "fyndpos":"mongodb://fynd_fyndpos_logs_readwrite:readWrite_fyndpos_logs!2024@10.155.48.136:27017,10.155.48.119:27017/fyndpos_logs?replicaSet=re_extensions_logs_set&readPreference=secondaryPreferred",
    }
}

INDEX_TUPLES = {
    "inventory_summary_trace_logs" : [
        [("company_id",ASCENDING), ("created_on", ASCENDING), ("status", ASCENDING)],
        [("company_id" , ASCENDING), ("created_on", DESCENDING)],
        [("company_id",ASCENDING), ("created_on", ASCENDING), ("message", ASCENDING)],
        [("company_id",ASCENDING), ("seller_identifier", ASCENDING)]
    
    ],

    "trace_logs" : [
        [("seller_identifier", ASCENDING), ("store_code", ASCENDING)],
        [("company_id", ASCENDING), ("created_on", ASCENDING)],
        [("created_on", ASCENDING), ("seller_identifier", ASCENDING)],
        [("company_id", ASCENDING), ("status", ASCENDING), ("created_on", ASCENDING), ("seller_identifier", ASCENDING)],
        [("company_id", ASCENDING), ("status", ASCENDING), ("created_on", DESCENDING), ("seller_identifier", ASCENDING)],
        [("created_on", ASCENDING), ("status", ASCENDING), ("seller_identifier", ASCENDING)],
        [("seller_identifier", ASCENDING), ("company_id", ASCENDING), ("store_code", ASCENDING)],
        [("company_id", ASCENDING), ("store_id", ASCENDING), ("seller_identifier", ASCENDING)],
        [("company_id", ASCENDING), ("seller_identifier", ASCENDING)],
        [("trace_id", ASCENDING), ("type", ASCENDING)]
    ],

    "acknowledgement_logs" : [
        [("category", ASCENDING), ("event", ASCENDING)],
        [("company_id", ASCENDING), ("type", ASCENDING), ("category", ASCENDING), ("modified_on", ASCENDING)],
        [("modified_on", ASCENDING), ("type", ASCENDING), ("category", ASCENDING)],
        [("created_on", DESCENDING)],
        [("_id", ASCENDING), ("type", ASCENDING)]
    ],

    "shipment_event_log" : [
        [("modified_on", ASCENDING), ("status", ASCENDING), ("retry_count", ASCENDING)],
        [("status", ASCENDING)],
        [("modified_on", ASCENDING)]
    ]


}