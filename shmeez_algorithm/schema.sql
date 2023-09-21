-- MySQL dump 10.13  Distrib 8.1.0, for macos11.7 (arm64)
--
-- Host: localhost    Database: POGOR
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `charge_move_stats`
--

DROP TABLE IF EXISTS `charge_move_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `charge_move_stats` (
  `Move` varchar(50) DEFAULT NULL,
  `Type` varchar(50) DEFAULT NULL,
  `Power` int DEFAULT NULL,
  `DPE` int DEFAULT NULL,
  `CD` int DEFAULT NULL,
  `DPS` double DEFAULT NULL,
  `EPS` double DEFAULT NULL,
  `DPS*DPE` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `DPS`
--

DROP TABLE IF EXISTS `DPS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DPS` (
  `name` varchar(255) DEFAULT NULL,
  `type1` varchar(255) DEFAULT NULL,
  `Charge_move` varchar(255) DEFAULT NULL,
  `Fast_move` varchar(255) DEFAULT NULL,
  `DPS` float DEFAULT NULL,
  `TDO` float DEFAULT NULL,
  `Total` float DEFAULT NULL,
  `type2` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event` (
  `col_0` varchar(255) DEFAULT NULL,
  `col_1` varchar(255) DEFAULT NULL,
  `col_2` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fast_move_stats`
--

DROP TABLE IF EXISTS `fast_move_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fast_move_stats` (
  `Move` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `power` int DEFAULT NULL,
  `energy` int DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `Damage` varchar(255) DEFAULT NULL,
  `Energy1` varchar(255) DEFAULT NULL,
  `Total` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hundred_pokemon`
--

DROP TABLE IF EXISTS `hundred_pokemon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hundred_pokemon` (
  `Index` int DEFAULT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Form` varchar(255) DEFAULT NULL,
  `Pokemon` int DEFAULT NULL,
  `Gender` varchar(255) DEFAULT NULL,
  `CP` int DEFAULT NULL,
  `HP` int DEFAULT NULL,
  `Atk` varchar(255) DEFAULT NULL,
  `Def` varchar(255) DEFAULT NULL,
  `Sta` varchar(255) DEFAULT NULL,
  `IV` varchar(255) DEFAULT NULL,
  `Level1` varchar(255) DEFAULT NULL,
  `Level2` varchar(255) DEFAULT NULL,
  `Quick` varchar(255) DEFAULT NULL,
  `Charge1` varchar(255) DEFAULT NULL,
  `Charge2` varchar(255) DEFAULT NULL,
  `Scan` varchar(255) DEFAULT NULL,
  `Catch` varchar(255) DEFAULT NULL,
  `Weight` varchar(255) DEFAULT NULL,
  `Height` varchar(255) DEFAULT NULL,
  `Lucky` int DEFAULT NULL,
  `Shadow_Purified` int DEFAULT NULL,
  `Favorite` int DEFAULT NULL,
  `Dust` int DEFAULT NULL,
  `Rank` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `my_pokemon`
--

DROP TABLE IF EXISTS `my_pokemon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `my_pokemon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `species` varchar(255) DEFAULT NULL,
  `level` int DEFAULT NULL,
  `fast_move` varchar(255) DEFAULT NULL,
  `charge_move` varchar(255) DEFAULT NULL,
  `cp` int DEFAULT NULL,
  `hp` int DEFAULT NULL,
  `attack` int DEFAULT NULL,
  `defense` int DEFAULT NULL,
  `stamina` int DEFAULT NULL,
  `shiny` varchar(1) DEFAULT NULL,
  `legacy` int DEFAULT NULL,
  `purified` int DEFAULT NULL,
  `lucky` int DEFAULT NULL,
  `trade` int DEFAULT NULL,
  `hundo` int DEFAULT NULL,
  `lucky_hundo` int DEFAULT NULL,
  `iv` int DEFAULT NULL,
  `iv_pct` int DEFAULT NULL,
  `appraisal` varchar(255) DEFAULT NULL,
  `attack_iv` int DEFAULT NULL,
  `defense_iv` int DEFAULT NULL,
  `stamina_iv` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `species_stats`
--

DROP TABLE IF EXISTS `species_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `species_stats` (
  `species_id` int NOT NULL,
  `species_name` varchar(50) DEFAULT NULL,
  `base_attack` int DEFAULT NULL,
  `base_defense` int DEFAULT NULL,
  `base_stamina` int DEFAULT NULL,
  `type1` varchar(20) DEFAULT NULL,
  `type2` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`species_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `type_effectiveness`
--

DROP TABLE IF EXISTS `type_effectiveness`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_effectiveness` (
  `Attacking` varchar(255) DEFAULT NULL,
  `Normal` int DEFAULT NULL,
  `Fire` int DEFAULT NULL,
  `Water` int DEFAULT NULL,
  `Electric` int DEFAULT NULL,
  `Grass` int DEFAULT NULL,
  `Ice` int DEFAULT NULL,
  `Fighting` int DEFAULT NULL,
  `Poison` float DEFAULT NULL,
  `Ground` int DEFAULT NULL,
  `Flying` int DEFAULT NULL,
  `Psychic` int DEFAULT NULL,
  `Bug` int DEFAULT NULL,
  `Rock` int DEFAULT NULL,
  `Ghost` int DEFAULT NULL,
  `Dragon` int DEFAULT NULL,
  `Dark` int DEFAULT NULL,
  `Steel` int DEFAULT NULL,
  `Fairy` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-21 13:06:31
