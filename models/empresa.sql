-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 24-11-2025 a las 15:44:23
-- Versión del servidor: 8.0.44-0ubuntu0.24.04.1
-- Versión de PHP: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `empresa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Departamento`
--

CREATE TABLE `Departamento` (
  `departamento_id` int NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `ubicacion` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `Departamento`
--

INSERT INTO `Departamento` (`departamento_id`, `nombre`, `ubicacion`) VALUES
(1, 'Sistemas / TI', 'Oficina Central - Servidores');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `DetalleProyecto`
--

CREATE TABLE `DetalleProyecto` (
  `detalle_proyecto_id` int NOT NULL,
  `empleado_id` int NOT NULL,
  `proyecto_id` int NOT NULL,
  `fecha_asignacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `rol_en_proyecto` varchar(100) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `horas_asignadas` int DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Empleado`
--

CREATE TABLE `Empleado` (
  `empleado_id` int NOT NULL,
  `usuario_id` int DEFAULT NULL,
  `departamento_id` int NOT NULL,
  `rol_id` int NOT NULL,
  `codigo_empleado` varchar(20) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `nombre` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `apellido` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `direccion` varchar(200) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `telefono` varchar(20) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `Empleado`
--

INSERT INTO `Empleado` (`empleado_id`, `usuario_id`, `departamento_id`, `rol_id`, `codigo_empleado`, `nombre`, `apellido`, `direccion`, `telefono`, `email`) VALUES
(1, 1, 1, 1, 'SYS-001', 'Super', 'Admin', NULL, NULL, 'admin@empresa.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Proyecto`
--

CREATE TABLE `Proyecto` (
  `proyecto_id` int NOT NULL,
  `nombre_proyecto` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_termino` date DEFAULT NULL,
  `descripcion` text COLLATE utf8mb3_spanish_ci,
  `estado` enum('Planificación','En Progreso','Finalizado','Pausado') COLLATE utf8mb3_spanish_ci DEFAULT 'Planificación'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `RegistroTiempo`
--

CREATE TABLE `RegistroTiempo` (
  `registro_id` int NOT NULL,
  `empleado_id` int NOT NULL,
  `proyecto_id` int NOT NULL,
  `fecha` date NOT NULL,
  `horas_trabajo` decimal(5,2) NOT NULL,
  `descripcion` varchar(255) COLLATE utf8mb3_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Rol`
--

CREATE TABLE `Rol` (
  `rol_id` int NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` varchar(255) COLLATE utf8mb3_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `Rol`
--

INSERT INTO `Rol` (`rol_id`, `nombre`, `descripcion`) VALUES
(1, 'Administrador del Sistema', 'Acceso total a todos los módulos y configuración');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Usuario`
--

CREATE TABLE `Usuario` (
  `usuario_id` int NOT NULL,
  `nombre_usuario` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL,
  `hash_password` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  `fecha_ultimo_acceso` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `Usuario`
--

INSERT INTO `Usuario` (`usuario_id`, `nombre_usuario`, `hash_password`, `fecha_ultimo_acceso`) VALUES
(1, 'admin', '12345', '2025-11-24 12:32:44');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Departamento`
--
ALTER TABLE `Departamento`
  ADD PRIMARY KEY (`departamento_id`);

--
-- Indices de la tabla `DetalleProyecto`
--
ALTER TABLE `DetalleProyecto`
  ADD PRIMARY KEY (`detalle_proyecto_id`),
  ADD KEY `FK_Detalle_Empleado` (`empleado_id`),
  ADD KEY `FK_Detalle_Proyecto` (`proyecto_id`);

--
-- Indices de la tabla `Empleado`
--
ALTER TABLE `Empleado`
  ADD PRIMARY KEY (`empleado_id`),
  ADD UNIQUE KEY `unique_email` (`email`),
  ADD UNIQUE KEY `unique_usuario` (`usuario_id`),
  ADD KEY `FK_Empleado_Depto` (`departamento_id`),
  ADD KEY `FK_Empleado_Rol` (`rol_id`);

--
-- Indices de la tabla `Proyecto`
--
ALTER TABLE `Proyecto`
  ADD PRIMARY KEY (`proyecto_id`);

--
-- Indices de la tabla `RegistroTiempo`
--
ALTER TABLE `RegistroTiempo`
  ADD PRIMARY KEY (`registro_id`),
  ADD KEY `FK_Registro_Empleado` (`empleado_id`),
  ADD KEY `FK_Registro_Proyecto` (`proyecto_id`);

--
-- Indices de la tabla `Rol`
--
ALTER TABLE `Rol`
  ADD PRIMARY KEY (`rol_id`);

--
-- Indices de la tabla `Usuario`
--
ALTER TABLE `Usuario`
  ADD PRIMARY KEY (`usuario_id`),
  ADD UNIQUE KEY `unique_user` (`nombre_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Departamento`
--
ALTER TABLE `Departamento`
  MODIFY `departamento_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `DetalleProyecto`
--
ALTER TABLE `DetalleProyecto`
  MODIFY `detalle_proyecto_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Empleado`
--
ALTER TABLE `Empleado`
  MODIFY `empleado_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `Proyecto`
--
ALTER TABLE `Proyecto`
  MODIFY `proyecto_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `RegistroTiempo`
--
ALTER TABLE `RegistroTiempo`
  MODIFY `registro_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Rol`
--
ALTER TABLE `Rol`
  MODIFY `rol_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `Usuario`
--
ALTER TABLE `Usuario`
  MODIFY `usuario_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `DetalleProyecto`
--
ALTER TABLE `DetalleProyecto`
  ADD CONSTRAINT `FK_Detalle_Empleado` FOREIGN KEY (`empleado_id`) REFERENCES `Empleado` (`empleado_id`),
  ADD CONSTRAINT `FK_Detalle_Proyecto` FOREIGN KEY (`proyecto_id`) REFERENCES `Proyecto` (`proyecto_id`);

--
-- Filtros para la tabla `Empleado`
--
ALTER TABLE `Empleado`
  ADD CONSTRAINT `FK_Empleado_Depto` FOREIGN KEY (`departamento_id`) REFERENCES `Departamento` (`departamento_id`),
  ADD CONSTRAINT `FK_Empleado_Rol` FOREIGN KEY (`rol_id`) REFERENCES `Rol` (`rol_id`),
  ADD CONSTRAINT `FK_Empleado_Usuario` FOREIGN KEY (`usuario_id`) REFERENCES `Usuario` (`usuario_id`);

--
-- Filtros para la tabla `RegistroTiempo`
--
ALTER TABLE `RegistroTiempo`
  ADD CONSTRAINT `FK_Registro_Empleado` FOREIGN KEY (`empleado_id`) REFERENCES `Empleado` (`empleado_id`),
  ADD CONSTRAINT `FK_Registro_Proyecto` FOREIGN KEY (`proyecto_id`) REFERENCES `Proyecto` (`proyecto_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
