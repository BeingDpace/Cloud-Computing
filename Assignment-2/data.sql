-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2021 at 04:54 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dpace`
--

-- --------------------------------------------------------

--
-- Table structure for table `foods`
--

CREATE TABLE `foods` (
  `id` int(11) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `classify` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `foods`
--

INSERT INTO `foods` (`id`, `image`, `name`, `price`, `description`, `classify`) VALUES
(1, 'pineapple.jpg', 'Pineapple', 129, '', 'fruit'),
(2, 'bread.jpg', 'Bread', 249, 'delicious dark healthy bread in the morning for breakfast', 'other'),
(3, 'figs.jpg', 'Figs', 408, '', 'fruit'),
(4, 'carrot.jpg', 'Carrot', 109, '', 'vegi'),
(5, 'cake.jpg', 'Cake', 329, '', 'other'),
(6, 'icecream.jpg', 'Ice Cream', 10, '', 'other'),
(7, 'lemon.jpg', 'Lemon', 20, 'full of vitamins and good in many deserts and meals', 'fruit'),
(8, 'asparagus.jpg', 'Asparagus', 89, '', 'vegi'),
(9, 'ginger.jpg', 'Ginger', 709, 'this is a different bread a dark rustic wheat', 'vegi'),
(10, 'avocado.jpg', 'Avocado', 45, '', 'fruit'),
(11, 'bread.jpg', 'Dark Bread', 119, '', 'other'),
(12, 'apple.jpg', 'Apple', 189, 'there are many types of apples this one is red delicious', 'fruit'),
(13, 'garlic.jpg', 'Garlic', 99, 'pairs well with both coffee and cake', 'fruit'),
(14, 'peach.jpg', 'Peach', 239, '', 'fruit'),
(15, 'tomato.jpg', 'Tomato', 40, 'vine ripe red juicy tomato healthy and tasty', 'fruit'),
(16, 'pears.jpg', 'Pears', 499, '', 'fruit'),
(17, 'watermelon.jpg', 'Watermelon', 599, '', 'fruit'),
(18, 'coffee.jpg', 'Coffee', 135, 'for the morning afternoon or pick me up late at night', 'other'),
(19, 'brocolli.jpg', 'Brocolli', 30, 'steamed boiled baked or raw a healthy tasty food', 'vegi'),
(20, 'corn.jpg', 'Corn', 488, '', 'vegi'),
(21, 'peanuts.jpg', 'Peanuts', 80, 'peanuts can be used for peanut oil for butter and many other', 'others'),
(22, 'cherry.jpg', 'Cherry', 90, '', 'fruit');

-- --------------------------------------------------------

--
-- Table structure for table `user_review`
--

CREATE TABLE `user_review` (
  `id` int(11) NOT NULL,
  `food_id` int(11) DEFAULT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_review`
--

INSERT INTO `user_review` (`id`, `food_id`, `user_name`, `comment`) VALUES
(19, 1, 'Deepesh', 'Delicious'),
(20, 1, 'Bishal', 'YUCK'),
(21, 2, 'Deepesh', '5 STAR'),
(22, 2, 'Bishal', '1 STAR'),
(23, 1, 'Noob Bishal', 'Noob Fruit');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `foods`
--
ALTER TABLE `foods`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_review`
--
ALTER TABLE `user_review`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_review_ibfk_1` (`food_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `foods`
--
ALTER TABLE `foods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `user_review`
--
ALTER TABLE `user_review`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
