
use pt_analyse;

-- ----------------------------
-- Table structure for service_type
-- ----------------------------
CREATE TABLE  service_type  (
   type_id        BIGINT(8)        NOT NULL PRIMARY KEY,
   type_name      varchar(100)    NOT NULL UNIQUE,
   type_desc      varchar(300)    default 'none'   NOT NULL,
   type_baseurl   varchar(300)    NOT NULL UNIQUE,
   type_level     TINYINT(1)       default 1        NOT NULL,
   type_uplevel   BIGINT(8)        default 10000000 NOT NULL,
   type_date      DATETIME         default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
   type_status    TINYINT(1)       default false    NOT NULL
)

;


-- ----------------------------
-- Table structure for service_info
-- ----------------------------
CREATE TABLE  service_info  (
   service_id     BIGINT(8)        NOT NULL PRIMARY KEY,
   service_type	  BIGINT(8) 			 NOT NULL,
   service_name   varchar(100)    NOT NULL UNIQUE ,
   service_desc   varchar(300)    default 'none'  NOT NULL,
   service_url    varchar(100)    default 'none'  NOT NULL,
   service_func   varchar(100)    default 'none'  NOT NULL,
   service_owner  varchar(50)     default 'none'  NOT NULL,
   service_date   DATETIME         DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
   service_status TINYINT(1)       default false   NOT NULL,
   FOREIGN KEY (service_type)REFERENCES service_type(type_id)
)

;

-- ----------------------------
-- Table structure for service_info
-- ----------------------------
CREATE TABLE  task_info  (
   task_id      varchar(100)    NOT NULL PRIMARY KEY,
   service_id	  BIGINT(8) 			 NOT NULL,
   task_begin   DATETIME         DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
   task_end     DATETIME         ,
   task_message varchar(500)    default 'none'  NOT NULL,
   task_status   TINYINT(1)      default 0  NOT NULL,

   FOREIGN KEY (service_id)REFERENCES service_info(service_id)
)

;


-- ----------------------------
-- Table structure for app_system
-- ----------------------------
CREATE TABLE  app_system  (
   app_id  varchar(20)     NOT NULL,
   app_ename  varchar(50)     NOT NULL,
   app_cname  varchar(200)     NOT NULL,
   app_cname_sub  varchar(200)     NOT NULL,
   center_name  varchar(100)     NOT NULL,
   level_flag  varchar(20)     NOT NULL,
   service_flag  varchar(20)     NOT NULL,
   app_manager  varchar(100)     NOT NULL,
   flag  varchar(10)    
)
 
;

-- ----------------------------
-- Table structure for change_control
-- ----------------------------
CREATE TABLE  change_control  (
   table_id  varchar(20)     NOT NULL,
   table_name_old  varchar(100)     NOT NULL DEFAULT 'none' ,
   table_name_new  varchar(100)     NOT NULL DEFAULT 'none' ,
   table_size  varchar(20)     NOT NULL DEFAULT 'none' ,
   table_temp  varchar(100)     NOT NULL DEFAULT 'none' ,
   table_time  varchar(20)     NOT NULL DEFAULT 'none' ,
   table_code  varchar(20)     NOT NULL DEFAULT 'none' ,
   table_user  varchar(20)     NOT NULL DEFAULT 'none' ,
   change_group  varchar(20)     NOT NULL DEFAULT '00000' ,
   change_time  varchar(20)     NOT NULL DEFAULT 'none' ,
   change_system  varchar(20)     NOT NULL DEFAULT 'none' ,
   change_logical  varchar(20)     NOT NULL DEFAULT 'none' ,
   change_number  varchar(20)     NOT NULL DEFAULT 'none' ,
   change_operator  varchar(20)     NOT NULL DEFAULT '000000' ,
   change_auditor  varchar(20)     NOT NULL DEFAULT '000000' ,
   change_desc  varchar(500)     NOT NULL DEFAULT 'none' 
)
 
;

-- ----------------------------
-- Table structure for company_info
-- ----------------------------
CREATE TABLE  company_info  (
   company_id  varchar(8)     NOT NULL,
   company_ch  varchar(50)     NOT NULL,
   company_en  varchar(50)     NOT NULL,
   company_abbr_cn  varchar(50)     NOT NULL,
   company_abbr_en  varchar(50)     NOT NULL
)
;

-- ----------------------------
-- Table structure for dang_info
-- ----------------------------
CREATE TABLE  dang_info  (
   table_name  varchar(1000)     NOT NULL,
   table_desc  varchar(1000)     NOT NULL DEFAULT 'none' 
)
 
;

-- ----------------------------
-- Table structure for dep_info
-- ----------------------------
CREATE TABLE  dep_info  (
   dq_id  varchar(20)     NOT NULL,
   dep_id  varchar(20)     NOT NULL,
   dep_name  varchar(500)     NOT NULL
)
;

-- ----------------------------
-- Table structure for develop_center
-- ----------------------------
CREATE TABLE  develop_center  (
   center_id  varchar(50)     NOT NULL,
   center_name  varchar(50)     NOT NULL,
   desc1  varchar(200)    ,
   desc2  varchar(200)    
)
;

-- ----------------------------
-- Table structure for dq_info
-- ----------------------------
CREATE TABLE  dq_info  (
   dq_id  varchar(20)     NOT NULL,
   dq_name  varchar(500)     NOT NULL,
   dp_location  varchar(500)     NOT NULL
)
;

-- ----------------------------
-- Table structure for duty_arrangment
-- ----------------------------
CREATE TABLE  duty_arrangment  (
   duty_date  varchar(20)     NOT NULL,
   duty_week  varchar(20)     NOT NULL,
   duty_id  varchar(20)     NOT NULL,
   staff_id  varchar(20)     NOT NULL
)
;

-- ----------------------------
-- Table structure for duty_arrangment_history
-- ----------------------------
CREATE TABLE  duty_arrangment_history  (
   duty_date  varchar(20)     NOT NULL,
   duty_id  varchar(20)     NOT NULL,
   duty_start  int4 NOT NULL,
   duty_offset_start  int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for duty_info
-- ----------------------------
CREATE TABLE  duty_info  (
   duty_id  varchar(20)     NOT NULL,
   duty_name  varchar(500)     NOT NULL,
   duty_duration  varchar(500)     NOT NULL,
   duty_desc  varchar(500)     NOT NULL,
   duty_start  int4,
   duty_offset  int4,
   duty_except  varchar(500)    ,
   duty_last_start  int4,
   duty_offset_start  int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for group_info
-- ----------------------------
CREATE TABLE  group_info  (
   dq_id  varchar(20)     NOT NULL,
   dep_id  varchar(20)     NOT NULL,
   group_id  varchar(20)     NOT NULL,
   group_name  varchar(500)     NOT NULL,
   group_desc  varchar(500)     NOT NULL
)
;

-- ----------------------------
-- Table structure for hard_bind_logical
-- ----------------------------
CREATE TABLE  hard_bind_logical  (
   hardware_id  varchar(20)     NOT NULL,
   logical_id  varchar(20)     NOT NULL
)
;

-- ----------------------------
-- Table structure for hardware_info
-- ----------------------------
CREATE TABLE  hardware_info  (
   hardware_id  varchar(20)     NOT NULL,
   type_id  varchar(20)     NOT NULL,
   dep_id  varchar(8)     NOT NULL,
   hardware_sn  varchar(50)     NOT NULL,
   cpu_num  varchar(10)     NOT NULL,
   mem_num  varchar(10)     NOT NULL,
   location1  varchar(200)     NOT NULL,
   location2  varchar(100)     NOT NULL,
   flag  varchar(10)     NOT NULL,
   summit_user  varchar(20)    
)
;

-- ----------------------------
-- Table structure for hoilday_calendar
-- ----------------------------
CREATE TABLE  hoilday_calendar  (
   hoilday_date  varchar(20)     NOT NULL,
   hoilday_desc  varchar(500)     NOT NULL,
   holiday_shift_flag  varchar(20)     NOT NULL
)
;

-- ----------------------------
-- Table structure for logical_info
-- ----------------------------
CREATE TABLE  logical_info  (
   logical_id  varchar(20)     NOT NULL,
   dep_id  varchar(8)     NOT NULL,
   logical_name  varchar(50)     NOT NULL,
   logical_type  varchar(50)     NOT NULL,
   cpu_num  varchar(10)     NOT NULL,
   mem_num  varchar(10)     NOT NULL,
   os_type_id  varchar(20)     NOT NULL,
   logical_unit  varchar(100)     NOT NULL,
   logical_usage  varchar(100)     NOT NULL,
   logical_comment  varchar(200)     NOT NULL,
   flag  varchar(10)     NOT NULL,
   summit_user  varchar(20)     NOT NULL
)
;

-- ----------------------------
-- Table structure for logical_model_type
-- ----------------------------
CREATE TABLE  logical_model_type  (
   type_id  varchar(20)     NOT NULL,
   company_id  varchar(8)     NOT NULL,
   type_desc  varchar(50)     NOT NULL,
   type_desc2  varchar(50)     NOT NULL,
   model_desc  varchar(50)     NOT NULL,
   model_desc2  varchar(50)     NOT NULL,
   model_desc3  varchar(200)     NOT NULL
)
 
;

-- ----------------------------
-- Table structure for logical_type
-- ----------------------------
CREATE TABLE  logical_type  (
   type_id  varchar(50)     NOT NULL,
   type_desc  varchar(50)     NOT NULL
)
 
;

-- ----------------------------
-- Table structure for machine_phy_type
-- ----------------------------
CREATE TABLE  machine_phy_type  (
   type_id  varchar(20)     NOT NULL,
   company_id  varchar(8)     NOT NULL,
   type_desc  varchar(50)     NOT NULL,
   type_desc2  varchar(50)     NOT NULL,
   model_desc  varchar(50)     NOT NULL
)
;

-- ----------------------------
-- Table structure for machine_type
-- ----------------------------
CREATE TABLE  machine_type  (
   type_id  varchar(50)     NOT NULL,
   type_desc  varchar(50)     NOT NULL
)
;

-- ----------------------------
-- Table structure for menu_info
-- ----------------------------
CREATE TABLE  menu_info  (
   menu_id  varchar(20)     NOT NULL,
   menu_name  varchar(500)     NOT NULL,
   menu_desc  varchar(500)     NOT NULL DEFAULT 'none' 
)
 
;

-- ----------------------------
-- Table structure for menu_privilige
-- ----------------------------
CREATE TABLE  menu_privilige  (
   menu_id  varchar(20)     NOT NULL,
   staff_id  varchar(20)     NOT NULL,
   menu_privilige  varchar(10)     NOT NULL DEFAULT 'R' 
)
 
;

-- ----------------------------
-- Table structure for modify_history
-- ----------------------------
CREATE TABLE  modify_history  (
   op_type  varchar(50)     NOT NULL,
   op_object  varchar(100)     NOT NULL,
   op_key  varchar(100)     NOT NULL,
   op_content  varchar(1000)     NOT NULL,
   op_time  varchar(20)     NOT NULL,
   op_user  varchar(50)     NOT NULL
)
 
;

-- ----------------------------
-- Table structure for ora_check_item
-- ----------------------------
CREATE TABLE  ora_check_item  (
   odc_check_id  int8 NOT NULL ,
   odc_check_type  varchar(100)     NOT NULL,
   odc_check_item  varchar(500)     NOT NULL,
   odc_check_level  varchar(50)     NOT NULL
)
 
;

-- ----------------------------
-- Table structure for ora_dailycheck
-- ----------------------------
CREATE TABLE  ora_dailycheck  (
   odc_id  int8 NOT NULL  ,
   odc_system  varchar(50)     NOT NULL,
   odc_machine  varchar(50)     NOT NULL,
   odc_instance  varchar(50)     NOT NULL,
   odc_a_role_id  varchar(50)     DEFAULT 'none' ,
   odc_a_role_nm  varchar(50)     DEFAULT 'none' 
)
 
;

-- ----------------------------
-- Table structure for ora_dailycheck_result
-- ----------------------------
CREATE TABLE  ora_dailycheck_result  (
   odc_id  int8 NOT NULL,
   odc_idsub  int8 NOT NULL ,
   odc_type  varchar(100)     NOT NULL,
   odc_item  varchar(200)     NOT NULL,
   odc_object  varchar(200)     DEFAULT 'none' ,
   odc_update  varchar(50)     NOT NULL,
   odc_times  varchar(50)     NOT NULL,
   odc_result  varchar(50)     NOT NULL,
   odc_value  varchar(300)     NOT NULL,
   odc_threshold  varchar(50)     NOT NULL,
   odc_date  varchar(50)     DEFAULT 'none' ,
   odc_status  varchar(50)     DEFAULT 'Uncomfirmed' ,
   odc_confirm_id  varchar(50)     DEFAULT 'none' ,
   odc_confirm_co  varchar(300)     DEFAULT 'none' ,
   odc_confirm_su  varchar(300)     DEFAULT 'none' ,
   odc_confirm_ty  varchar(300)     DEFAULT 'none' ,
   odc_confirm_st  varchar(100)     DEFAULT 'none' ,
   odc_confirm_ti  varchar(50)     DEFAULT 'none' 
)
 
;

-- ----------------------------
-- Table structure for regular_info
-- ----------------------------
CREATE TABLE  regular_info  (
   staff_id  varchar(20)     NOT NULL,
   staff_dep_id  varchar(20)     NOT NULL,
   staff_name  varchar(500)     NOT NULL,
   staff_title  varchar(500)     NOT NULL,
   staff_sex  varchar(500)     NOT NULL,
   staff_duty  varchar(500)     NOT NULL,
   staff_tel  varchar(100)     NOT NULL,
   staff_cell  varchar(100)     NOT NULL,
   staff_email  varchar(100)     NOT NULL,
   staff_place  varchar(500)     NOT NULL,
   staff_weigth  int4 NOT NULL,
   staff_company  varchar(500)     NOT NULL,
   staff_group_id  varchar(20)    ,
   staff_dep_tmp_id  varchar(20)    
)
;

-- ----------------------------
-- Table structure for service_level
-- ----------------------------
CREATE TABLE  service_level  (
   service_id  varchar(20)     NOT NULL,
   service_flag  varchar(20)     NOT NULL,
   desc1  varchar(200)    ,
   desc2  varchar(200)    
)
;

-- ----------------------------
-- Table structure for sms_history
-- ----------------------------
CREATE TABLE  sms_history  (
   sms_date  varchar(30)    ,
   sms_place  varchar(500)    ,
   sms_dep  varchar(500)    ,
   sms_sys  varchar(500)    ,
   sms_msg  varchar(500)    ,
   sms_tail  varchar(500)    ,
   sms_notice  varchar(1000)    
)
;

-- ----------------------------
-- Table structure for software_model_type
-- ----------------------------
CREATE TABLE  software_model_type  (
   type_id  varchar(20)     NOT NULL,
   company_id  varchar(8)     NOT NULL,
   type_desc  varchar(50)     NOT NULL,
   type_desc2  varchar(50)     NOT NULL,
   model_desc  varchar(50)     NOT NULL,
   model_desc2  varchar(50)     NOT NULL,
   model_desc3  varchar(200)     NOT NULL
)
;

-- ----------------------------
-- Table structure for software_type
-- ----------------------------
CREATE TABLE  software_type  (
   type_id  varchar(50)     NOT NULL,
   type_desc  varchar(50)     NOT NULL
)
;

-- ----------------------------
-- Table structure for staff_bind_logical
-- ----------------------------
CREATE TABLE  staff_bind_logical  (
   staff_id  varchar(20)     NOT NULL,
   logical_id  varchar(20)     NOT NULL,
   staff_id_b  varchar(20)    
)
;

-- ----------------------------
-- Table structure for staff_calendar
-- ----------------------------
CREATE TABLE  staff_calendar  (
   staff_date  varchar(20)     NOT NULL,
   staff_desc  varchar(500)     NOT NULL,
   staff_shift_flag  varchar(20)     NOT NULL
)
;

-- ----------------------------
-- Table structure for staff_phone
-- ----------------------------
CREATE TABLE  staff_phone  (
   staff_id  varchar(20)    ,
   phone_imei  varchar(500)    ,
   phone_date  varchar(20)    ,
   phone_stat  varchar(10)    
)
;

-- ----------------------------
-- Table structure for staff_software_skill
-- ----------------------------
CREATE TABLE  staff_software_skill  (
   unique_id  varchar(20)     NOT NULL,
   staff_id  varchar(20)     NOT NULL,
   type_id  varchar(20)     NOT NULL
)
;

-- ----------------------------
-- Table structure for status_info
-- ----------------------------
CREATE TABLE  status_info  (
   status_id  varchar(20)     NOT NULL,
   status_type  varchar(20)     NOT NULL,
   status_desc  varchar(50)     NOT NULL,
   status_comment  varchar(100)     NOT NULL
)
 
;

-- ----------------------------
-- Table structure for sys_knowlege
-- ----------------------------
CREATE TABLE  sys_knowlege  (
   kg_id  varchar(20)     NOT NULL,
   kg_title  varchar(500)     NOT NULL DEFAULT 'none' ,
   kg_system  varchar(20)     NOT NULL DEFAULT 'none' ,
   kg_process  varchar(2000)     NOT NULL DEFAULT 'none' ,
   kg_keys  varchar(500)     NOT NULL DEFAULT 'none' ,
   kg_time  varchar(20)     NOT NULL DEFAULT 'none' ,
   kg_user  varchar(20)     NOT NULL DEFAULT 'none' ,
   kg_dep  varchar(20)     NOT NULL DEFAULT 'none' 
)
 
;

-- ----------------------------
-- Table structure for system_level
-- ----------------------------
CREATE TABLE  system_level  (
   level_id  varchar(20)     NOT NULL,
   level_flag  varchar(20)     NOT NULL,
   desc1  varchar(200)    ,
   desc2  varchar(200)    
)
;

-- ----------------------------
-- Table structure for table_info
-- ----------------------------
CREATE TABLE  table_info  (
   table_name  varchar(500)     NOT NULL,
   table_desc  varchar(500)     NOT NULL DEFAULT 'none' 
)
 
;

-- ----------------------------
-- Table structure for template_bind_logical
-- ----------------------------
CREATE TABLE  template_bind_logical  (
   template_id  varchar(20)     NOT NULL,
   logical_id  varchar(20)     NOT NULL
)
 
;

-- ----------------------------
-- Table structure for template_item
-- ----------------------------
CREATE TABLE  template_item  (
   item_id  varchar(20)     NOT NULL,
   template_id  varchar(50)     NOT NULL,
   item_name  varchar(50)     NOT NULL,
   item_desc  varchar(100)     NOT NULL
)
 
;

-- ----------------------------
-- Table structure for template_logical_data
-- ----------------------------
CREATE TABLE  template_logical_data  (
   data_id  varchar(20)     NOT NULL,
   item_id  varchar(20)     NOT NULL,
   template_id  varchar(50)     NOT NULL,
   logical_id  varchar(20)     NOT NULL,
   item_value  varchar(200)     NOT NULL
)
 
;

-- ----------------------------
-- Table structure for template_object
-- ----------------------------
CREATE TABLE  template_object  (
   object_id  varchar(20)     NOT NULL,
   object_name  varchar(50)     NOT NULL,
   object_desc  varchar(100)     NOT NULL
)
 
;

-- ----------------------------
-- Table structure for template_type
-- ----------------------------
CREATE TABLE  template_type  (
   template_id  varchar(20)     NOT NULL,
   type_id  varchar(50)     NOT NULL,
   desc_name  varchar(100)     NOT NULL,
   desc_comm  varchar(200)     NOT NULL,
   object_id  varchar(20)    ,
   mode_id  varchar(50)    
)
 
;

-- ----------------------------
-- Table structure for usage_type
-- ----------------------------
CREATE TABLE  usage_type  (
   type_id  varchar(50)     NOT NULL,
   type_desc  varchar(50)     NOT NULL
)
;

-- ----------------------------
-- Table structure for user_privilege
-- ----------------------------
CREATE TABLE  user_privilege  (
   user_id  varchar(100)     NOT NULL,
   user_pw  varchar(20)     NOT NULL DEFAULT 'password' ,
   user_pr  varchar(100)     NOT NULL DEFAULT 'none' 
)
;

-- ----------------------------
-- Table structure for vote_info
-- ----------------------------
CREATE TABLE  vote_info  (
   vote_id  varchar(20)    ,
   vote_name  varchar(500)    ,
   vote_items  varchar(2)    ,
   vote_start  varchar(20)    ,
   vote_end  varchar(20)    ,
   vote_choice  varchar(2)    ,
   vote_flag  varchar(1)    
)
;

-- ----------------------------
-- Table structure for wsms_process
-- ----------------------------
CREATE TABLE  wsms_process  (
   wsms_id  varchar(20)     NOT NULL,
   wsms_title  varchar(500)     NOT NULL DEFAULT 'none' ,
   wsms_template  varchar(500)     NOT NULL DEFAULT 'none' ,
   wsms_process  varchar(2000)     NOT NULL DEFAULT 'none' ,
   wsms_keys  varchar(500)     NOT NULL DEFAULT 'none' ,
   wsms_time  varchar(20)     NOT NULL DEFAULT 'none' ,
   wsms_user  varchar(20)     NOT NULL DEFAULT 'none' ,
   wsms_dep  varchar(20)     NOT NULL DEFAULT 'none' 
)
 
;

-- ----------------------------
-- Indexes structure for table app_bind_logical
-- ----------------------------
CREATE UNIQUE INDEX  app_bind_logical_app_id_logical_id_idx  ON  app_bind_logical   (
   app_id        ,
   logical_id        
)  ;
CREATE UNIQUE INDEX  app_bind_logical_logical_id_idx  ON  app_bind_logical   (
   logical_id        
)  ;

-- ----------------------------
-- Indexes structure for table app_system
-- ----------------------------
CREATE UNIQUE INDEX  app_system_app_cname_app_cname_sub_idx  ON  app_system   (
   app_cname        ,
   app_cname_sub        
)  ;
CREATE UNIQUE INDEX  app_system_app_ename_app_cname_sub_idx  ON  app_system   (
   app_ename        ,
   app_cname_sub        
)  ;
CREATE UNIQUE INDEX  app_system_app_id_idx  ON  app_system   (
   app_id        
)  ;

-- ----------------------------
-- Primary Key structure for table change_control
-- ----------------------------
ALTER TABLE  change_control  ADD CONSTRAINT  change_control_pkey  PRIMARY KEY ( table_id )    ;

-- ----------------------------
-- Indexes structure for table company_info
-- ----------------------------
CREATE UNIQUE INDEX  company_info_company_abbr_cn_idx  ON  company_info   (
   company_abbr_cn        
);
CREATE UNIQUE INDEX  company_info_company_abbr_en_idx  ON  company_info   (
   company_abbr_en        
);
CREATE UNIQUE INDEX  company_info_company_id_idx  ON  company_info   (
   company_id        
);

-- ----------------------------
-- Primary Key structure for table dang_info
-- ----------------------------
ALTER TABLE  dang_info  ADD CONSTRAINT  dang_info_pkey  PRIMARY KEY ( table_name )    ;

-- ----------------------------
-- Indexes structure for table dep_info
-- ----------------------------
CREATE UNIQUE INDEX  dep_info_dep_id_idx  ON  dep_info   (
   dep_id        
);
CREATE UNIQUE INDEX  dep_info_dq_id_dep_id_idx  ON  dep_info   (
   dq_id        ,
   dep_id        
);

-- ----------------------------
-- Indexes structure for table develop_center
-- ----------------------------
CREATE UNIQUE INDEX  develop_center_center_id_idx  ON  develop_center   (
   center_id        
);
CREATE UNIQUE INDEX  develop_center_center_name_idx  ON  develop_center   (
   center_name        
);

-- ----------------------------
-- Indexes structure for table dq_info
-- ----------------------------
CREATE UNIQUE INDEX  dq_info_dq_id_idx  ON  dq_info   (
   dq_id        
);

-- ----------------------------
-- Indexes structure for table duty_arrangment
-- ----------------------------
CREATE UNIQUE INDEX  duty_arrangment_duty_date_staff_id_duty_id_idx  ON  duty_arrangment   (
   duty_date        ,
   staff_id        ,
   duty_id        
);

-- ----------------------------
-- Indexes structure for table duty_arrangment_history
-- ----------------------------
CREATE UNIQUE INDEX  duty_arrangment_history_duty_date_duty_id_idx  ON  duty_arrangment_history   (
   duty_date        ,
   duty_id        
);

-- ----------------------------
-- Indexes structure for table duty_info
-- ----------------------------
CREATE UNIQUE INDEX  duty_info_duty_id_idx  ON  duty_info   (
   duty_id        
);
CREATE UNIQUE INDEX  duty_info_duty_name_idx  ON  duty_info   (
   duty_name        
);

-- ----------------------------
-- Indexes structure for table group_info
-- ----------------------------
CREATE UNIQUE INDEX  group_info_dq_id_dep_id_group_id_idx  ON  group_info   (
   dq_id        ,
   dep_id        ,
   group_id        
);
CREATE UNIQUE INDEX  group_info_group_id_idx  ON  group_info   (
   group_id        
);

-- ----------------------------
-- Indexes structure for table hard_bind_logical
-- ----------------------------
CREATE UNIQUE INDEX  hard_bind_logical_hardware_id_logical_id_idx  ON  hard_bind_logical   (
   hardware_id        ,
   logical_id        
);
CREATE UNIQUE INDEX  hard_bind_logical_logical_id_idx  ON  hard_bind_logical   (
   logical_id        
)  ;

-- ----------------------------
-- Indexes structure for table hardware_info
-- ----------------------------
CREATE UNIQUE INDEX  hardware_info_hardware_id_idx  ON  hardware_info   (
   hardware_id        
);
CREATE UNIQUE INDEX  hardware_info_location1_location2_idx  ON  hardware_info   (
   location1        ,
   location2        
);
CREATE UNIQUE INDEX  hardware_info_type_id_hardware_sn_idx  ON  hardware_info   (
   type_id        ,
   hardware_sn        
);

-- ----------------------------
-- Indexes structure for table hoilday_calendar
-- ----------------------------
CREATE UNIQUE INDEX  hoilday_calendar_hoilday_date_idx  ON  hoilday_calendar   (
   hoilday_date        
);

-- ----------------------------
-- Indexes structure for table logical_info
-- ----------------------------
CREATE UNIQUE INDEX  logical_info_logical_id_idx  ON  logical_info   (
   logical_id        
);
CREATE UNIQUE INDEX  logical_info_logical_name_idx  ON  logical_info   (
   logical_name        
);

-- ----------------------------
-- Indexes structure for table logical_model_type
-- ----------------------------
CREATE UNIQUE INDEX  logical_model_type_type_desc_model_desc_idx  ON  logical_model_type   (
   type_desc        ,
   model_desc        
)  ;
CREATE UNIQUE INDEX  logical_model_type_type_id_idx  ON  logical_model_type   (
   type_id        
)  ;

-- ----------------------------
-- Indexes structure for table logical_type
-- ----------------------------
CREATE UNIQUE INDEX  logical_type_type_desc_idx  ON  logical_type   (
   type_desc        
)  ;
CREATE UNIQUE INDEX  logical_type_type_id_idx  ON  logical_type   (
   type_id        
)  ;

-- ----------------------------
-- Indexes structure for table machine_phy_type
-- ----------------------------
CREATE UNIQUE INDEX  machine_phy_type_company_id_model_desc_type_desc_idx  ON  machine_phy_type   (
   company_id        ,
   model_desc        ,
   type_desc        
);
CREATE UNIQUE INDEX  machine_phy_type_type_id_idx  ON  machine_phy_type   (
   type_id        
);

-- ----------------------------
-- Indexes structure for table machine_type
-- ----------------------------
CREATE UNIQUE INDEX  machine_type_type_desc_idx  ON  machine_type   (
   type_desc        
);
CREATE UNIQUE INDEX  machine_type_type_id_idx  ON  machine_type   (
   type_id        
);

-- ----------------------------
-- Indexes structure for table menu_info
-- ----------------------------
CREATE UNIQUE INDEX  menu_info_menu_id_idx  ON  menu_info   (
   menu_id        
)  ;
CREATE UNIQUE INDEX  menu_info_menu_name_idx  ON  menu_info   (
   menu_name        
)  ;

-- ----------------------------
-- Indexes structure for table menu_privilige
-- ----------------------------
CREATE UNIQUE INDEX  menu_privilige_menu_id_staff_id_idx  ON  menu_privilige   (
   menu_id        ,
   staff_id        
)  ;

-- ----------------------------
-- Indexes structure for table ora_check_item
-- ----------------------------
CREATE UNIQUE INDEX  ora_check_item_odc_check_id_idx  ON  ora_check_item   (
   odc_check_type        ,
   odc_check_item        
)  ;

-- ----------------------------
-- Primary Key structure for table ora_check_item
-- ----------------------------
ALTER TABLE  ora_check_item  ADD CONSTRAINT  ora_check_item_pkey  PRIMARY KEY ( odc_check_id )    ;

-- ----------------------------
-- Indexes structure for table ora_dailycheck
-- ----------------------------
CREATE UNIQUE INDEX  ora_dailycheck_odc_object_idx  ON  ora_dailycheck   (
   odc_system        ,
   odc_machine        ,
   odc_instance        
)  ;

-- ----------------------------
-- Primary Key structure for table ora_dailycheck
-- ----------------------------
ALTER TABLE  ora_dailycheck  ADD CONSTRAINT  ora_dailycheck_pkey  PRIMARY KEY ( odc_id )    ;

-- ----------------------------
-- Indexes structure for table ora_dailycheck_result
-- ----------------------------
CREATE UNIQUE INDEX  ora_dailycheck_result_idx  ON  ora_dailycheck_result   (
   odc_id   ,
   odc_type        ,
   odc_item        ,
   odc_object        ,
   odc_times        ,
   odc_date        
)  ;

-- ----------------------------
-- Primary Key structure for table ora_dailycheck_result
-- ----------------------------
ALTER TABLE  ora_dailycheck_result  ADD CONSTRAINT  ora_dailycheck_result_pkey  PRIMARY KEY ( odc_idsub )    ;

-- ----------------------------
-- Indexes structure for table regular_info
-- ----------------------------
CREATE UNIQUE INDEX  regular_info_staff_email_idx  ON  regular_info   (
   staff_email        
);
CREATE UNIQUE INDEX  regular_info_staff_id_idx  ON  regular_info   (
   staff_id        
);

-- ----------------------------
-- Indexes structure for table service_level
-- ----------------------------
CREATE UNIQUE INDEX  service_level_service_flag_idx  ON  service_level   (
   service_flag        
);
CREATE UNIQUE INDEX  service_level_service_id_idx  ON  service_level   (
   service_id        
);

-- ----------------------------
-- Indexes structure for table sms_history
-- ----------------------------
CREATE UNIQUE INDEX  sms_history_sms_date_sms_sys_idx  ON  sms_history   (
   sms_date        ,
   sms_sys        
);

-- ----------------------------
-- Indexes structure for table software_model_type
-- ----------------------------
CREATE UNIQUE INDEX  software_model_type_type_desc2_idx  ON  software_model_type   (
   type_desc2        
);
CREATE UNIQUE INDEX  software_model_type_type_id_idx  ON  software_model_type   (
   type_id        
);

-- ----------------------------
-- Indexes structure for table software_type
-- ----------------------------
CREATE UNIQUE INDEX  software_type_type_desc_idx  ON  software_type   (
   type_desc        
);
CREATE UNIQUE INDEX  software_type_type_id_idx  ON  software_type   (
   type_id        
);

-- ----------------------------
-- Indexes structure for table staff_bind_logical
-- ----------------------------
CREATE UNIQUE INDEX  staff_bind_logical_staff_id_logical_id_idx  ON  staff_bind_logical   (
   staff_id        ,
   logical_id        
);

-- ----------------------------
-- Indexes structure for table staff_calendar
-- ----------------------------
CREATE UNIQUE INDEX  staff_calendar_staff_date_idx  ON  staff_calendar   (
   staff_date        
);

-- ----------------------------
-- Indexes structure for table staff_phone
-- ----------------------------
CREATE UNIQUE INDEX  staff_phone_phone_imei_idx  ON  staff_phone   (
   phone_imei        
);
CREATE UNIQUE INDEX  staff_phone_staff_id_idx  ON  staff_phone   (
   staff_id        
);

-- ----------------------------
-- Indexes structure for table staff_software_skill
-- ----------------------------
CREATE INDEX  staff_software_skill_staff_id_idx  ON  staff_software_skill   (
   staff_id        
);
CREATE INDEX  staff_software_skill_type_id_idx  ON  staff_software_skill   (
   type_id        
);
CREATE UNIQUE INDEX  staff_software_skill_unique_id_idx  ON  staff_software_skill   (
   unique_id        
);

-- ----------------------------
-- Indexes structure for table status_info
-- ----------------------------
CREATE UNIQUE INDEX  status_info_status_id_idx  ON  status_info   (
   status_id        
)  ;
CREATE UNIQUE INDEX  status_info_status_type_idx  ON  status_info   (
   status_type        
)  ;
CREATE UNIQUE INDEX  status_info_status_type_status_desc_idx  ON  status_info   (
   status_type        ,
   status_desc        
)  ;

-- ----------------------------
-- Indexes structure for table sys_knowlege
-- ----------------------------
CREATE UNIQUE INDEX  kg_title_kg_title_idx  ON  sys_knowlege   (
   kg_title        
)  ;

-- ----------------------------
-- Primary Key structure for table sys_knowlege
-- ----------------------------
ALTER TABLE  sys_knowlege  ADD CONSTRAINT  sys_knowlege_pkey  PRIMARY KEY ( kg_id )    ;

-- ----------------------------
-- Indexes structure for table system_level
-- ----------------------------
CREATE UNIQUE INDEX  system_level_level_flag_idx  ON  system_level   (
   level_flag        
);
CREATE UNIQUE INDEX  system_level_level_id_idx  ON  system_level   (
   level_id        
);

-- ----------------------------
-- Primary Key structure for table table_info
-- ----------------------------
ALTER TABLE  table_info  ADD CONSTRAINT  table_info_pkey  PRIMARY KEY ( table_name )    ;

-- ----------------------------
-- Indexes structure for table template_bind_logical
-- ----------------------------
CREATE UNIQUE INDEX  template_bind_logical_logical_id_idx  ON  template_bind_logical   (
   logical_id        
)  ;

-- ----------------------------
-- Indexes structure for table template_item
-- ----------------------------
CREATE UNIQUE INDEX  template_item_item_id_idx  ON  template_item   (
   item_id        
)  ;
CREATE UNIQUE INDEX  template_item_template_id_item_name_idx  ON  template_item   (
   template_id        ,
   item_name        
)  ;

-- ----------------------------
-- Indexes structure for table template_logical_data
-- ----------------------------
CREATE UNIQUE INDEX  template_logical_data_data_id_idx  ON  template_logical_data   (
   data_id        
)  ;
CREATE UNIQUE INDEX  template_logical_data_logical_id_template_id_item_id_idx  ON  template_logical_data   (
   logical_id        ,
   template_id        ,
   item_id        
)  ;

-- ----------------------------
-- Indexes structure for table template_object
-- ----------------------------
CREATE UNIQUE INDEX  template_object_object_id_idx  ON  template_object   (
   object_id        
)  ;
CREATE UNIQUE INDEX  template_object_object_name_idx  ON  template_object   (
   object_name        
)  ;

-- ----------------------------
-- Indexes structure for table template_type
-- ----------------------------
CREATE UNIQUE INDEX  template_type_desc_name_idx  ON  template_type   (
   desc_name        
)  ;
CREATE UNIQUE INDEX  template_type_template_id_idx  ON  template_type   (
   template_id        
)  ;

-- ----------------------------
-- Indexes structure for table usage_type
-- ----------------------------
CREATE UNIQUE INDEX  usage_type_type_desc_idx  ON  usage_type   (
   type_desc        
);
CREATE UNIQUE INDEX  usage_type_type_id_idx  ON  usage_type   (
   type_id        
);

-- ----------------------------
-- Indexes structure for table vote_info
-- ----------------------------
CREATE UNIQUE INDEX  vote_info_vote_id_vote_items_vote_flag_idx  ON  vote_info   (
   vote_id        ,
   vote_items        ,
   vote_flag        
);
CREATE UNIQUE INDEX  vote_info_vote_id_vote_name_idx  ON  vote_info   (
   vote_id        ,
   vote_name        
);

-- ----------------------------
-- Indexes structure for table wsms_process
-- ----------------------------
CREATE UNIQUE INDEX  wsms_process_wsms_title_idx  ON  wsms_process   (
   wsms_title        
)  ;

-- ----------------------------
-- Primary Key structure for table wsms_process
-- ----------------------------
ALTER TABLE  wsms_process  ADD CONSTRAINT  wsms_process_pkey  PRIMARY KEY ( wsms_id )    ;

-- ----------------------------
-- Foreign Keys structure for table app_bind_logical
-- ----------------------------
ALTER TABLE  app_bind_logical  ADD CONSTRAINT  app_bind_logical_app_id_fkey  FOREIGN KEY ( app_id ) REFERENCES  app_system  ( app_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  app_bind_logical  ADD CONSTRAINT  app_bind_logical_logical_id_fkey  FOREIGN KEY ( logical_id ) REFERENCES  logical_info  ( logical_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table app_system
-- ----------------------------
ALTER TABLE  app_system  ADD CONSTRAINT  app_system_center_name_fkey  FOREIGN KEY ( center_name ) REFERENCES  develop_center  ( center_name ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  app_system  ADD CONSTRAINT  app_system_level_flag_fkey  FOREIGN KEY ( level_flag ) REFERENCES  system_level  ( level_flag ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  app_system  ADD CONSTRAINT  app_system_service_flag_fkey  FOREIGN KEY ( service_flag ) REFERENCES  service_level  ( service_flag ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table change_control
-- ----------------------------
ALTER TABLE  change_control  ADD CONSTRAINT  change_auditor_fk  FOREIGN KEY ( change_auditor ) REFERENCES  regular_info  ( staff_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  change_control  ADD CONSTRAINT  change_group_fk  FOREIGN KEY ( change_group ) REFERENCES  group_info  ( group_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  change_control  ADD CONSTRAINT  change_operator_fk  FOREIGN KEY ( change_operator ) REFERENCES  regular_info  ( staff_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table dep_info
-- ----------------------------
ALTER TABLE  dep_info  ADD CONSTRAINT  dep_info_dq_id_fkey  FOREIGN KEY ( dq_id ) REFERENCES  dq_info  ( dq_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table duty_arrangment
-- ----------------------------
ALTER TABLE  duty_arrangment  ADD CONSTRAINT  duty_arrangment_duty_id_fkey  FOREIGN KEY ( duty_id ) REFERENCES  duty_info  ( duty_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  duty_arrangment  ADD CONSTRAINT  duty_arrangment_staff_id_fkey  FOREIGN KEY ( staff_id ) REFERENCES  regular_info  ( staff_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table duty_arrangment_history
-- ----------------------------
ALTER TABLE  duty_arrangment_history  ADD CONSTRAINT  duty_arrangment_history_duty_id_fkey  FOREIGN KEY ( duty_id ) REFERENCES  duty_info  ( duty_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table group_info
-- ----------------------------
ALTER TABLE  group_info  ADD CONSTRAINT  group_info_dep_id_fkey  FOREIGN KEY ( dep_id ) REFERENCES  dep_info  ( dep_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  group_info  ADD CONSTRAINT  group_info_dq_id_fkey  FOREIGN KEY ( dq_id ) REFERENCES  dq_info  ( dq_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table hard_bind_logical
-- ----------------------------
ALTER TABLE  hard_bind_logical  ADD CONSTRAINT  hard_bind_logical_hardware_id_fkey  FOREIGN KEY ( hardware_id ) REFERENCES  hardware_info  ( hardware_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  hard_bind_logical  ADD CONSTRAINT  hard_bind_logical_logical_id_fkey  FOREIGN KEY ( logical_id ) REFERENCES  logical_info  ( logical_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table hardware_info
-- ----------------------------
ALTER TABLE  hardware_info  ADD CONSTRAINT  hardware_info_dep_id_fkey  FOREIGN KEY ( dep_id ) REFERENCES  dep_info  ( dep_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  hardware_info  ADD CONSTRAINT  hardware_info_type_id_fkey  FOREIGN KEY ( type_id ) REFERENCES  machine_phy_type  ( type_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table logical_info
-- ----------------------------
ALTER TABLE  logical_info  ADD CONSTRAINT  logical_info_dep_id_fkey  FOREIGN KEY ( dep_id ) REFERENCES  dep_info  ( dep_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  logical_info  ADD CONSTRAINT  logical_info_logical_usage_fk  FOREIGN KEY ( logical_usage ) REFERENCES  usage_type  ( type_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  logical_info  ADD CONSTRAINT  logical_info_os_type_id_fkey  FOREIGN KEY ( os_type_id ) REFERENCES  software_model_type  ( type_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table machine_phy_type
-- ----------------------------
ALTER TABLE  machine_phy_type  ADD CONSTRAINT  machine_phy_type_company_id_fkey  FOREIGN KEY ( company_id ) REFERENCES  company_info  ( company_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  machine_phy_type  ADD CONSTRAINT  type_desc_fk  FOREIGN KEY ( type_desc ) REFERENCES  machine_type  ( type_desc ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table menu_privilige
-- ----------------------------
ALTER TABLE  menu_privilige  ADD CONSTRAINT  menu_privilige_menu_id_fkey  FOREIGN KEY ( menu_id ) REFERENCES  menu_info  ( menu_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  menu_privilige  ADD CONSTRAINT  menu_privilige_staff_id_fkey  FOREIGN KEY ( staff_id ) REFERENCES  regular_info  ( staff_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table modify_history
-- ----------------------------
ALTER TABLE  modify_history  ADD CONSTRAINT  op_object_fk  FOREIGN KEY ( op_object ) REFERENCES  table_info  ( table_name ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table ora_dailycheck_result
-- ----------------------------
ALTER TABLE  ora_dailycheck_result  ADD CONSTRAINT  odc_id_fk  FOREIGN KEY ( odc_id ) REFERENCES  ora_dailycheck  ( odc_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table regular_info
-- ----------------------------
ALTER TABLE  regular_info  ADD CONSTRAINT  regular_info_staff_dep_id_fkey  FOREIGN KEY ( staff_dep_id ) REFERENCES  dep_info  ( dep_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  regular_info  ADD CONSTRAINT  regular_info_staff_group_id_fkey  FOREIGN KEY ( staff_group_id ) REFERENCES  group_info  ( group_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table software_model_type
-- ----------------------------
ALTER TABLE  software_model_type  ADD CONSTRAINT  software_model_type_company_id_fkey  FOREIGN KEY ( company_id ) REFERENCES  company_info  ( company_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  software_model_type  ADD CONSTRAINT  software_type_fk1  FOREIGN KEY ( type_desc ) REFERENCES  software_type  ( type_desc ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table staff_bind_logical
-- ----------------------------
ALTER TABLE  staff_bind_logical  ADD CONSTRAINT  staff_bind_logical_logical_id_fkey  FOREIGN KEY ( logical_id ) REFERENCES  logical_info  ( logical_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  staff_bind_logical  ADD CONSTRAINT  staff_bind_logical_staff_id_fkey  FOREIGN KEY ( staff_id ) REFERENCES  regular_info  ( staff_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table staff_phone
-- ----------------------------
ALTER TABLE  staff_phone  ADD CONSTRAINT  staff_phone_staff_id_fkey  FOREIGN KEY ( staff_id ) REFERENCES  regular_info  ( staff_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table staff_software_skill
-- ----------------------------
ALTER TABLE  staff_software_skill  ADD CONSTRAINT  staff_software_skill_staff_id_fkey  FOREIGN KEY ( staff_id ) REFERENCES  regular_info  ( staff_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  staff_software_skill  ADD CONSTRAINT  staff_software_skill_type_id_fkey  FOREIGN KEY ( type_id ) REFERENCES  software_model_type  ( type_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table sys_knowlege
-- ----------------------------
ALTER TABLE  sys_knowlege  ADD CONSTRAINT  kg_system_fk  FOREIGN KEY ( kg_system ) REFERENCES  app_system  ( app_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table template_bind_logical
-- ----------------------------
ALTER TABLE  template_bind_logical  ADD CONSTRAINT  template_bind_logical_logical_id_fkey  FOREIGN KEY ( logical_id ) REFERENCES  logical_info  ( logical_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  template_bind_logical  ADD CONSTRAINT  template_bind_logical_template_id_fkey  FOREIGN KEY ( template_id ) REFERENCES  template_type  ( template_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table template_item
-- ----------------------------
ALTER TABLE  template_item  ADD CONSTRAINT  template_item_template_id_fkey  FOREIGN KEY ( template_id ) REFERENCES  template_type  ( template_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table template_logical_data
-- ----------------------------
ALTER TABLE  template_logical_data  ADD CONSTRAINT  template_logical_data_item_id_fkey  FOREIGN KEY ( item_id ) REFERENCES  template_item  ( item_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  template_logical_data  ADD CONSTRAINT  template_logical_data_logical_id_fkey  FOREIGN KEY ( logical_id ) REFERENCES  logical_info  ( logical_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  template_logical_data  ADD CONSTRAINT  template_logical_data_logical_id_fkey2  FOREIGN KEY ( logical_id ) REFERENCES  template_bind_logical  ( logical_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE  template_logical_data  ADD CONSTRAINT  template_logical_data_template_id_fkey  FOREIGN KEY ( template_id ) REFERENCES  template_type  ( template_id ) ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table template_type
-- ----------------------------
ALTER TABLE  template_type  ADD CONSTRAINT  FOREIGN KEY ( object_id ) REFERENCES  template_object  ( object_id ) ;

-- ----------------------------
-- Foreign Keys structure for table user_privilege
-- ----------------------------
ALTER TABLE  user_privilege  ADD CONSTRAINT  user_privilege_user_id_fkey  FOREIGN KEY ( user_id ) REFERENCES  regular_info  ( staff_email ) ;

-- ----------------------------
-- Foreign Keys structure for table wsms_process
-- ----------------------------
ALTER TABLE  wsms_process  ADD CONSTRAINT  wsms_dep_fk  FOREIGN KEY ( wsms_dep ) REFERENCES  dep_info  ( dep_id ) ;
