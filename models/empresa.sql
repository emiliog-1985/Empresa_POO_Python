-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 10-12-2025 a las 01:26:25
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
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `departamento_id` int NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `ubicacion` varchar(150) COLLATE utf8mb3_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`departamento_id`, `nombre`, `ubicacion`) VALUES
(1, 'Sistemas / TI', 'Oficina Central - Servidores'),
(2, 'RR.HH', 'Departamento de recursos Humanos Empresa.LTDA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalleproyecto`
--

CREATE TABLE `detalleproyecto` (
  `detalle_proyecto_id` int NOT NULL,
  `empleado_id` int NOT NULL,
  `proyecto_id` int NOT NULL,
  `fecha_asignacion` datetime DEFAULT CURRENT_TIMESTAMP,
  `rol_en_proyecto` varchar(100) COLLATE utf8mb3_spanish_ci DEFAULT NULL,
  `horas_asignadas` int DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
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
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`empleado_id`, `usuario_id`, `departamento_id`, `rol_id`, `codigo_empleado`, `nombre`, `apellido`, `direccion`, `telefono`, `email`) VALUES
(1, 1, 1, 1, 'SYS-01', 'Administrador', 'Sistemas', 'localhost', '+56984710029', 'admin@localhost'),
(2, 3, 2, 3, 'SOC-01', 'Veronica', 'Albornoz', 'Gonzalo Cerda #1481', '+56984710029', 'veronica.albornoz.gonzalez@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `proyecto_id` int NOT NULL,
  `nombre_proyecto` varchar(100) COLLATE utf8mb3_spanish_ci NOT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_termino` date DEFAULT NULL,
  `descripcion` text COLLATE utf8mb3_spanish_ci,
  `estado` enum('Planificación','En Progreso','Finalizado','Pausado') COLLATE utf8mb3_spanish_ci DEFAULT 'Planificación'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registrotiempo`
--

CREATE TABLE `registrotiempo` (
  `registro_id` int NOT NULL,
  `empleado_id` int NOT NULL,
  `proyecto_id` int NOT NULL,
  `fecha` date NOT NULL,
  `horas_trabajo` decimal(5,2) NOT NULL,
  `descripcion` varchar(255) COLLATE utf8mb3_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `rol_id` int NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL,
  `descripcion` varchar(255) COLLATE utf8mb3_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`rol_id`, `nombre`, `descripcion`) VALUES
(1, 'Administrador del Sistema', 'Acceso total a todos los módulos y configuración'),
(2, 'Gerente Empresa', 'Puede revisar todos los proyectos'),
(3, 'Empleado', 'Empleado de la Empresa.LTDA'),
(4, 'Personal Externo', 'Personal contratado para proyectos temporales');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `usuario_id` int NOT NULL,
  `nombre_usuario` varchar(50) COLLATE utf8mb3_spanish_ci NOT NULL,
  `hash_password` varchar(255) COLLATE utf8mb3_spanish_ci NOT NULL,
  `salt` varchar(32) COLLATE utf8mb3_spanish_ci NOT NULL,
  `fecha_ultimo_acceso` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`usuario_id`, `nombre_usuario`, `hash_password`, `salt`, `fecha_ultimo_acceso`) VALUES
(1, 'admin', '4972dd17041fb7868d7d7460d885f6f3b61657a780d12581bd9c9042c376baf6', '07250eb28668c24cc6742fc5331b320e', '2025-12-09 21:54:31'),
(2, 'emilio', '86e57e84995cf147287d1062641501fa7336bb6031fb12c1e79fdc95a0553344', '5afe44884ab3ef431b2b599d4c34f399', NULL),
(3, 'vero', '2385b8ee7b3915b9280b3133070b9df9435faa400f3261e5bb0629ca9e8975f3', '18c1bcd04137b011ef6ccfe62cac8e5b', '2025-12-09 00:44:15'),
(12, 'pepe', '7e7b4570f8d30e445d28eb6ffcea27968d7e6ba38fe220ec71d293291a92d854', 'fc415d1634948dc704023dcdf8b3a033', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`departamento_id`);

--
-- Indices de la tabla `detalleproyecto`
--
ALTER TABLE `detalleproyecto`
  ADD PRIMARY KEY (`detalle_proyecto_id`),
  ADD KEY `FK_Detalle_Empleado` (`empleado_id`),
  ADD KEY `FK_Detalle_Proyecto` (`proyecto_id`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`empleado_id`),
  ADD UNIQUE KEY `unique_email` (`email`),
  ADD UNIQUE KEY `unique_usuario` (`usuario_id`),
  ADD KEY `FK_Empleado_Depto` (`departamento_id`),
  ADD KEY `FK_Empleado_Rol` (`rol_id`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`proyecto_id`);

--
-- Indices de la tabla `registrotiempo`
--
ALTER TABLE `registrotiempo`
  ADD PRIMARY KEY (`registro_id`),
  ADD KEY `FK_Registro_Empleado` (`empleado_id`),
  ADD KEY `FK_Registro_Proyecto` (`proyecto_id`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`rol_id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`usuario_id`),
  ADD UNIQUE KEY `unique_user` (`nombre_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `departamento_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `detalleproyecto`
--
ALTER TABLE `detalleproyecto`
  MODIFY `detalle_proyecto_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `empleado_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `proyecto_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `registrotiempo`
--
ALTER TABLE `registrotiempo`
  MODIFY `registro_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `rol_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `usuario_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `detalleproyecto`
--
ALTER TABLE `detalleproyecto`
  ADD CONSTRAINT `FK_Detalle_Empleado` FOREIGN KEY (`empleado_id`) REFERENCES `empleado` (`empleado_id`),
  ADD CONSTRAINT `FK_Detalle_Proyecto` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`proyecto_id`);

--
-- Filtros para la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `FK_Empleado_Depto` FOREIGN KEY (`departamento_id`) REFERENCES `departamento` (`departamento_id`),
  ADD CONSTRAINT `FK_Empleado_Rol` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`rol_id`),
  ADD CONSTRAINT `FK_Empleado_Usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`);

--
-- Filtros para la tabla `registrotiempo`
--
ALTER TABLE `registrotiempo`
  ADD CONSTRAINT `FK_Registro_Empleado` FOREIGN KEY (`empleado_id`) REFERENCES `empleado` (`empleado_id`),
  ADD CONSTRAINT `FK_Registro_Proyecto` FOREIGN KEY (`proyecto_id`) REFERENCES `proyecto` (`proyecto_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
