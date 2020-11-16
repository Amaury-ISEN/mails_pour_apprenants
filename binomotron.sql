-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Oct 29, 2020 at 09:26 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `binomotron`
--

-- --------------------------------------------------------

--
-- Table structure for table `apprenants`
--

CREATE TABLE `apprenants` (
  `id_apprenant` int(11) NOT NULL,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `apprenants`
--

INSERT INTO `apprenants` (`id_apprenant`, `nom`, `prenom`, `photo`) VALUES
(1, 'Bonneau', 'Amaury', NULL),
(2, 'Pertron', 'Aude', NULL),
(3, 'Le Berre', 'Baptiste', NULL),
(4, 'Le Goff', 'Baptiste', NULL),
(5, 'Guillen', 'Celine', NULL),
(6, 'Karfaoui', 'Christelle', NULL),
(7, 'Mbarga Mvogo', 'Christian', NULL),
(8, 'Cloatre', 'Erwan', NULL),
(9, 'Moulard', 'Eva', NULL),
(10, 'Verpoest', 'Guillaume', NULL),
(11, 'Ibanni', 'Jamal', NULL),
(12, 'Le Joncour', 'Jérémy', NULL),
(13, 'Furiga', 'Julien', NULL),
(14, 'Maintier', 'Ludivine', NULL),
(15, 'Bokalli', 'Luigi', NULL),
(16, 'Le Moal', 'Patricia', NULL),
(17, 'Sabia', 'Paul', NULL),
(18, 'Hergoualc\'h', 'Pereg', NULL),
(19, 'Rioual', 'Ronan', NULL),
(20, 'Chaigneau', 'Thomas', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `apprenants_groupes`
--

CREATE TABLE `apprenants_groupes` (
  `id_apprenant` int(11) DEFAULT NULL,
  `id_groupe` int(11) DEFAULT NULL,
  `id_projet` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `groupes`
--

CREATE TABLE `groupes` (
  `id_groupe` int(11) NOT NULL,
  `libelle` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `projets`
--

CREATE TABLE `projets` (
  `id_projet` int(11) NOT NULL,
  `libelle` varchar(50) DEFAULT NULL,
  `date_debut` date DEFAULT NULL,
  `date_fin` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `apprenants`
--
ALTER TABLE `apprenants`
  ADD PRIMARY KEY (`id_apprenant`);

--
-- Indexes for table `apprenants_groupes`
--
ALTER TABLE `apprenants_groupes`
  ADD KEY `id_apprenant` (`id_apprenant`),
  ADD KEY `id_groupe` (`id_groupe`),
  ADD KEY `id_projet` (`id_projet`);

--
-- Indexes for table `groupes`
--
ALTER TABLE `groupes`
  ADD PRIMARY KEY (`id_groupe`);

--
-- Indexes for table `projets`
--
ALTER TABLE `projets`
  ADD PRIMARY KEY (`id_projet`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `apprenants`
--
ALTER TABLE `apprenants`
  MODIFY `id_apprenant` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `groupes`
--
ALTER TABLE `groupes`
  MODIFY `id_groupe` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projets`
--
ALTER TABLE `projets`
  MODIFY `id_projet` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `apprenants_groupes`
--
ALTER TABLE `apprenants_groupes`
  ADD CONSTRAINT `apprenants_groupes_ibfk_1` FOREIGN KEY (`id_apprenant`) REFERENCES `apprenants` (`id_apprenant`),
  ADD CONSTRAINT `apprenants_groupes_ibfk_2` FOREIGN KEY (`id_groupe`) REFERENCES `groupes` (`id_groupe`),
  ADD CONSTRAINT `apprenants_groupes_ibfk_3` FOREIGN KEY (`id_projet`) REFERENCES `projets` (`id_projet`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
