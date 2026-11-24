CREATE TABLE `pacientes` (
  `id` integer PRIMARY KEY,
  `raca` varchar(255),
  `genero` varchar(255),
  `data_nascimento` datetime
);

CREATE TABLE `medicao` (
  `id` integer PRIMARY KEY,
  `paciente_id` integer NOT NULL,
  `peso` decimal,
  `altura` decimal,
  `imc` decimal,
  `data_medicao` datetime
);

CREATE TABLE `faixa_etaria` (
  `id` integer PRIMARY KEY,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `problema` (
  `id` integer PRIMARY KEY,
  `codigo_problema` varchar(255) NOT NULL,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `diagnostico` (
  `id` integer PRIMARY KEY,
  `problema_id` integer NOT NULL,
  `internacao_id` integer NOT NULL
);

CREATE TABLE `exame_requisitado` (
  `id` integer PRIMARY KEY,
  `paciente_id` integer NOT NULL,
  `data_requisicao` datetime
);

CREATE TABLE `exame_max_glu_serum` (
  `id` integer PRIMARY KEY,
  `exame_requisitado_id` integer UNIQUE NOT NULL,
  `valor_exame` decimal NOT NULL
);

CREATE TABLE `exame_hbA1c` (
  `id` integer PRIMARY KEY,
  `exame_requisitado_id` integer UNIQUE NOT NULL,
  `valor_exame` decimal NOT NULL
);

CREATE TABLE `medicamento` (
  `id` integer PRIMARY KEY,
  `nome` varchar(255) NOT NULL,
  `substancia` varchar(255) NOT NULL
);

CREATE TABLE `administracao_medicamento` (
  `id` integer PRIMARY KEY,
  `internacao_id` integer NOT NULL,
  `medicamento_id` integer NOT NULL,
  `data_administracao` datetime
);

CREATE TABLE `pagamento` (
  `id` integer PRIMARY KEY,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `especialidade_medica` (
  `id` integer PRIMARY KEY,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `tipo_internacao` (
  `id` integer PRIMARY KEY,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `internacoes` (
  `id` integer PRIMARY KEY,
  `paciente_id` integer NOT NULL,
  `faixa_etaria_id` integer NOT NULL,
  `tipo_internacao_id` integer NOT NULL,
  `destino` varchar(255),
  `origem` varchar(255),
  `readmissao` boolean,
  `data_entrada` datetime,
  `data_saida` datetime,
  `pagamento_id` integer NOT NULL,
  `especialidade_medica_id` integer NOT NULL
);

ALTER TABLE `medicao` ADD FOREIGN KEY (`paciente_id`) REFERENCES `pacientes` (`id`);

ALTER TABLE `diagnostico` ADD FOREIGN KEY (`problema_id`) REFERENCES `problema` (`id`);

ALTER TABLE `diagnostico` ADD FOREIGN KEY (`internacao_id`) REFERENCES `internacoes` (`id`);

ALTER TABLE `exame_requisitado` ADD FOREIGN KEY (`paciente_id`) REFERENCES `pacientes` (`id`);

ALTER TABLE `exame_max_glu_serum` ADD FOREIGN KEY (`exame_requisitado_id`) REFERENCES `exame_requisitado` (`id`);

ALTER TABLE `exame_hbA1c` ADD FOREIGN KEY (`exame_requisitado_id`) REFERENCES `exame_requisitado` (`id`);

ALTER TABLE `administracao_medicamento` ADD FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id`);

ALTER TABLE `administracao_medicamento` ADD FOREIGN KEY (`internacao_id`) REFERENCES `internacoes` (`id`);

ALTER TABLE `internacoes` ADD FOREIGN KEY (`faixa_etaria_id`) REFERENCES `faixa_etaria` (`id`);

ALTER TABLE `internacoes` ADD FOREIGN KEY (`paciente_id`) REFERENCES `pacientes` (`id`);

ALTER TABLE `internacoes` ADD FOREIGN KEY (`tipo_internacao_id`) REFERENCES `tipo_internacao` (`id`);

ALTER TABLE `internacoes` ADD FOREIGN KEY (`pagamento_id`) REFERENCES `pagamento` (`id`);

ALTER TABLE `internacoes` ADD FOREIGN KEY (`especialidade_medica_id`) REFERENCES `especialidade_medica` (`id`);
