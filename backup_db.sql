/*
SQLyog Enterprise - MySQL GUI v6.13
MySQL - 5.7.14 : Database - db_student_mgmt_system
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

create database if not exists `db_student_mgmt_system`;

USE `db_student_mgmt_system`;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_customuser'),(22,'Can change user',6,'change_customuser'),(23,'Can delete user',6,'delete_customuser'),(24,'Can view user',6,'view_customuser'),(25,'Can add attendance',7,'add_attendance'),(26,'Can change attendance',7,'change_attendance'),(27,'Can delete attendance',7,'delete_attendance'),(28,'Can view attendance',7,'view_attendance'),(29,'Can add course',8,'add_course'),(30,'Can change course',8,'change_course'),(31,'Can delete course',8,'delete_course'),(32,'Can view course',8,'view_course'),(33,'Can add subjects',9,'add_subjects'),(34,'Can change subjects',9,'change_subjects'),(35,'Can delete subjects',9,'delete_subjects'),(36,'Can view subjects',9,'view_subjects'),(37,'Can add student',10,'add_student'),(38,'Can change student',10,'change_student'),(39,'Can delete student',10,'delete_student'),(40,'Can view student',10,'view_student'),(41,'Can add staff',11,'add_staff'),(42,'Can change staff',11,'change_staff'),(43,'Can delete staff',11,'delete_staff'),(44,'Can view staff',11,'view_staff'),(45,'Can add notification student',12,'add_notificationstudent'),(46,'Can change notification student',12,'change_notificationstudent'),(47,'Can delete notification student',12,'delete_notificationstudent'),(48,'Can view notification student',12,'view_notificationstudent'),(49,'Can add notification staff',13,'add_notificationstaff'),(50,'Can change notification staff',13,'change_notificationstaff'),(51,'Can delete notification staff',13,'delete_notificationstaff'),(52,'Can view notification staff',13,'view_notificationstaff'),(53,'Can add leave report student',14,'add_leavereportstudent'),(54,'Can change leave report student',14,'change_leavereportstudent'),(55,'Can delete leave report student',14,'delete_leavereportstudent'),(56,'Can view leave report student',14,'view_leavereportstudent'),(57,'Can add leave report staff',15,'add_leavereportstaff'),(58,'Can change leave report staff',15,'change_leavereportstaff'),(59,'Can delete leave report staff',15,'delete_leavereportstaff'),(60,'Can view leave report staff',15,'view_leavereportstaff'),(61,'Can add feed back student',16,'add_feedbackstudent'),(62,'Can change feed back student',16,'change_feedbackstudent'),(63,'Can delete feed back student',16,'delete_feedbackstudent'),(64,'Can view feed back student',16,'view_feedbackstudent'),(65,'Can add feed back staff',17,'add_feedbackstaff'),(66,'Can change feed back staff',17,'change_feedbackstaff'),(67,'Can delete feed back staff',17,'delete_feedbackstaff'),(68,'Can view feed back staff',17,'view_feedbackstaff'),(69,'Can add attendance report',18,'add_attendancereport'),(70,'Can change attendance report',18,'change_attendancereport'),(71,'Can delete attendance report',18,'delete_attendancereport'),(72,'Can view attendance report',18,'view_attendancereport'),(73,'Can add admin hod',19,'add_adminhod'),(74,'Can change admin hod',19,'change_adminhod'),(75,'Can delete admin hod',19,'delete_adminhod'),(76,'Can view admin hod',19,'view_adminhod');

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_student_m` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_student_m` FOREIGN KEY (`user_id`) REFERENCES `student_management_system_app_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(19,'student_management_system_app','adminhod'),(7,'student_management_system_app','attendance'),(18,'student_management_system_app','attendancereport'),(8,'student_management_system_app','course'),(6,'student_management_system_app','customuser'),(17,'student_management_system_app','feedbackstaff'),(16,'student_management_system_app','feedbackstudent'),(15,'student_management_system_app','leavereportstaff'),(14,'student_management_system_app','leavereportstudent'),(13,'student_management_system_app','notificationstaff'),(12,'student_management_system_app','notificationstudent'),(11,'student_management_system_app','staff'),(10,'student_management_system_app','student'),(9,'student_management_system_app','subjects');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2020-04-12 01:22:10.514412'),(2,'contenttypes','0002_remove_content_type_name','2020-04-12 01:22:10.622123'),(3,'auth','0001_initial','2020-04-12 01:22:10.760754'),(4,'auth','0002_alter_permission_name_max_length','2020-04-12 01:22:11.028039'),(5,'auth','0003_alter_user_email_max_length','2020-04-12 01:22:11.061950'),(6,'auth','0004_alter_user_username_opts','2020-04-12 01:22:11.076909'),(7,'auth','0005_alter_user_last_login_null','2020-04-12 01:22:11.090871'),(8,'auth','0006_require_contenttypes_0002','2020-04-12 01:22:11.097851'),(9,'auth','0007_alter_validators_add_error_messages','2020-04-12 01:22:11.111815'),(10,'auth','0008_alter_user_username_max_length','2020-04-12 01:22:11.125779'),(11,'auth','0009_alter_user_last_name_max_length','2020-04-12 01:22:11.138744'),(12,'auth','0010_alter_group_name_max_length','2020-04-12 01:22:11.182625'),(13,'auth','0011_update_proxy_permissions','2020-04-12 01:22:11.198583'),(14,'student_management_system_app','0001_initial','2020-04-12 01:22:12.208882'),(15,'admin','0001_initial','2020-04-12 01:22:13.935267'),(16,'admin','0002_logentry_remove_auto_add','2020-04-12 01:22:14.083882'),(17,'admin','0003_logentry_add_action_flag_choices','2020-04-12 01:22:14.112792'),(18,'sessions','0001_initial','2020-04-12 01:22:14.160665');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('chh2ove457fdtmlxvp3macofwfi5plsn','ZWRkYTQwODlmZTk3MTVkNmY3MTdlZWY5OTVhYzVlZTk0ZmQ0YWZlMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic3R1ZGVudF9tYW5hZ2VtZW50X3N5c3RlbV9hcHAuRW1haWxCYWNrRW5kLkVtYWlsQmFja0VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQ4NzNkZjZiNmI4Y2Y0ZDliZTNkZjM3NTk3YzQ3MGJlZjVlYzQxYjAifQ==','2020-04-26 01:34:03.402055'),('coq5igg1fy2k7k6ucoxr7c39w4830uy5','NDcwY2EzZjRmYTJkN2VmZGIwYTM0YjRlZjU5NTdhYzQ1NDY0MmNmYjp7fQ==','2020-04-26 01:27:03.974340');

/*Table structure for table `student_management_system_app_adminhod` */

DROP TABLE IF EXISTS `student_management_system_app_adminhod`;

CREATE TABLE `student_management_system_app_adminhod` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`),
  CONSTRAINT `student_management_s_admin_id_e257b5fd_fk_student_m` FOREIGN KEY (`admin_id`) REFERENCES `student_management_system_app_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_adminhod` */

insert  into `student_management_system_app_adminhod`(`id`,`created_at`,`updated_at`,`admin_id`) values (1,'2020-04-12 01:23:36.007312','2020-04-12 01:23:36.007312',1);

/*Table structure for table `student_management_system_app_attendance` */

DROP TABLE IF EXISTS `student_management_system_app_attendance`;

CREATE TABLE `student_management_system_app_attendance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attendance_date` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `subject_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_management_s_subject_id_id_68cbc17e_fk_student_m` (`subject_id_id`),
  CONSTRAINT `student_management_s_subject_id_id_68cbc17e_fk_student_m` FOREIGN KEY (`subject_id_id`) REFERENCES `student_management_system_app_subjects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_attendance` */

/*Table structure for table `student_management_system_app_attendancereport` */

DROP TABLE IF EXISTS `student_management_system_app_attendancereport`;

CREATE TABLE `student_management_system_app_attendancereport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `attendance_id_id` int(11) NOT NULL,
  `student_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_management_s_attendance_id_id_d40f803a_fk_student_m` (`attendance_id_id`),
  KEY `student_management_s_student_id_id_c6f446e0_fk_student_m` (`student_id_id`),
  CONSTRAINT `student_management_s_attendance_id_id_d40f803a_fk_student_m` FOREIGN KEY (`attendance_id_id`) REFERENCES `student_management_system_app_attendance` (`id`),
  CONSTRAINT `student_management_s_student_id_id_c6f446e0_fk_student_m` FOREIGN KEY (`student_id_id`) REFERENCES `student_management_system_app_student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_attendancereport` */

/*Table structure for table `student_management_system_app_course` */

DROP TABLE IF EXISTS `student_management_system_app_course`;

CREATE TABLE `student_management_system_app_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_course` */

insert  into `student_management_system_app_course`(`id`,`course_name`,`created_at`,`updated_at`) values (1,'Test Course','2020-04-12 01:24:53.031400','2020-04-12 01:24:53.031400');

/*Table structure for table `student_management_system_app_customuser` */

DROP TABLE IF EXISTS `student_management_system_app_customuser`;

CREATE TABLE `student_management_system_app_customuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_customuser` */

insert  into `student_management_system_app_customuser`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`,`user_type`) values (1,'pbkdf2_sha256$180000$T98Sc28MYZT0$SGyFMn0GKyIuzN053OSlHl5V1ajoFUbdqPBXlf4nK8M=','2020-04-12 01:34:03.397067',1,'admin','','','admin@mail.com',1,1,'2020-04-12 01:23:35.793882','1'),(2,'pbkdf2_sha256$180000$0rvy9VokSg3q$pjwbLCCn9nsLsf1Hma48V3QI58tNAFAmB94DrNDJ91Y=','2020-04-12 01:27:03.982318',0,'milson','Milson','Munakami','milsonmun@gmail.com',0,1,'2020-04-12 01:24:36.477653','2');

/*Table structure for table `student_management_system_app_customuser_groups` */

DROP TABLE IF EXISTS `student_management_system_app_customuser_groups`;

CREATE TABLE `student_management_system_app_customuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_management_syste_customuser_id_group_id_837cbdb6_uniq` (`customuser_id`,`group_id`),
  KEY `student_management_s_group_id_5abe657f_fk_auth_grou` (`group_id`),
  CONSTRAINT `student_management_s_customuser_id_280ee7ad_fk_student_m` FOREIGN KEY (`customuser_id`) REFERENCES `student_management_system_app_customuser` (`id`),
  CONSTRAINT `student_management_s_group_id_5abe657f_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_customuser_groups` */

/*Table structure for table `student_management_system_app_customuser_user_permissions` */

DROP TABLE IF EXISTS `student_management_system_app_customuser_user_permissions`;

CREATE TABLE `student_management_system_app_customuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_management_syste_customuser_id_permission_e35486e5_uniq` (`customuser_id`,`permission_id`),
  KEY `student_management_s_permission_id_58e3ea90_fk_auth_perm` (`permission_id`),
  CONSTRAINT `student_management_s_customuser_id_5c383f1e_fk_student_m` FOREIGN KEY (`customuser_id`) REFERENCES `student_management_system_app_customuser` (`id`),
  CONSTRAINT `student_management_s_permission_id_58e3ea90_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_customuser_user_permissions` */

/*Table structure for table `student_management_system_app_feedbackstaff` */

DROP TABLE IF EXISTS `student_management_system_app_feedbackstaff`;

CREATE TABLE `student_management_system_app_feedbackstaff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` longtext NOT NULL,
  `feedback_reply` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `staff_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_management_s_staff_id_id_ece0478d_fk_student_m` (`staff_id_id`),
  CONSTRAINT `student_management_s_staff_id_id_ece0478d_fk_student_m` FOREIGN KEY (`staff_id_id`) REFERENCES `student_management_system_app_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_feedbackstaff` */

/*Table structure for table `student_management_system_app_feedbackstudent` */

DROP TABLE IF EXISTS `student_management_system_app_feedbackstudent`;

CREATE TABLE `student_management_system_app_feedbackstudent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` longtext NOT NULL,
  `feedback_reply` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `student_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_management_s_student_id_id_247e6bbe_fk_student_m` (`student_id_id`),
  CONSTRAINT `student_management_s_student_id_id_247e6bbe_fk_student_m` FOREIGN KEY (`student_id_id`) REFERENCES `student_management_system_app_student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_feedbackstudent` */

/*Table structure for table `student_management_system_app_leavereportstaff` */

DROP TABLE IF EXISTS `student_management_system_app_leavereportstaff`;

CREATE TABLE `student_management_system_app_leavereportstaff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `leave_date` varchar(255) NOT NULL,
  `leave_message` longtext NOT NULL,
  `leave_status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `staff_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_management_s_staff_id_id_61b7c833_fk_student_m` (`staff_id_id`),
  CONSTRAINT `student_management_s_staff_id_id_61b7c833_fk_student_m` FOREIGN KEY (`staff_id_id`) REFERENCES `student_management_system_app_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_leavereportstaff` */

/*Table structure for table `student_management_system_app_leavereportstudent` */

DROP TABLE IF EXISTS `student_management_system_app_leavereportstudent`;

CREATE TABLE `student_management_system_app_leavereportstudent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `leave_date` varchar(255) NOT NULL,
  `leave_message` longtext NOT NULL,
  `leave_status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `student_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_management_s_student_id_id_b317db15_fk_student_m` (`student_id_id`),
  CONSTRAINT `student_management_s_student_id_id_b317db15_fk_student_m` FOREIGN KEY (`student_id_id`) REFERENCES `student_management_system_app_student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_leavereportstudent` */

/*Table structure for table `student_management_system_app_notificationstaff` */

DROP TABLE IF EXISTS `student_management_system_app_notificationstaff`;

CREATE TABLE `student_management_system_app_notificationstaff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `staff_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_management_s_staff_id_id_37f27ed9_fk_student_m` (`staff_id_id`),
  CONSTRAINT `student_management_s_staff_id_id_37f27ed9_fk_student_m` FOREIGN KEY (`staff_id_id`) REFERENCES `student_management_system_app_staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_notificationstaff` */

/*Table structure for table `student_management_system_app_notificationstudent` */

DROP TABLE IF EXISTS `student_management_system_app_notificationstudent`;

CREATE TABLE `student_management_system_app_notificationstudent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `student_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_management_s_student_id_id_2392edfd_fk_student_m` (`student_id_id`),
  CONSTRAINT `student_management_s_student_id_id_2392edfd_fk_student_m` FOREIGN KEY (`student_id_id`) REFERENCES `student_management_system_app_student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_notificationstudent` */

/*Table structure for table `student_management_system_app_staff` */

DROP TABLE IF EXISTS `student_management_system_app_staff`;

CREATE TABLE `student_management_system_app_staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`),
  CONSTRAINT `student_management_s_admin_id_6328179a_fk_student_m` FOREIGN KEY (`admin_id`) REFERENCES `student_management_system_app_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_staff` */

insert  into `student_management_system_app_staff`(`id`,`address`,`created_at`,`updated_at`,`admin_id`) values (1,'5035 S East End Ave APT 405N','2020-04-12 01:24:36.784834','2020-04-12 01:24:36.784834',2);

/*Table structure for table `student_management_system_app_student` */

DROP TABLE IF EXISTS `student_management_system_app_student`;

CREATE TABLE `student_management_system_app_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gender` varchar(255) NOT NULL,
  `profile_pic` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `session_start_year` date NOT NULL,
  `session_end_year` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `course_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`),
  KEY `student_management_s_course_id_id_01094f1c_fk_student_m` (`course_id_id`),
  CONSTRAINT `student_management_s_admin_id_f71c8366_fk_student_m` FOREIGN KEY (`admin_id`) REFERENCES `student_management_system_app_customuser` (`id`),
  CONSTRAINT `student_management_s_course_id_id_01094f1c_fk_student_m` FOREIGN KEY (`course_id_id`) REFERENCES `student_management_system_app_course` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_student` */

/*Table structure for table `student_management_system_app_subjects` */

DROP TABLE IF EXISTS `student_management_system_app_subjects`;

CREATE TABLE `student_management_system_app_subjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `course_id_id` int(11) NOT NULL,
  `staff_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_management_s_course_id_id_84084d4e_fk_student_m` (`course_id_id`),
  KEY `student_management_s_staff_id_id_9f975d57_fk_student_m` (`staff_id_id`),
  CONSTRAINT `student_management_s_course_id_id_84084d4e_fk_student_m` FOREIGN KEY (`course_id_id`) REFERENCES `student_management_system_app_course` (`id`),
  CONSTRAINT `student_management_s_staff_id_id_9f975d57_fk_student_m` FOREIGN KEY (`staff_id_id`) REFERENCES `student_management_system_app_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_management_system_app_subjects` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
