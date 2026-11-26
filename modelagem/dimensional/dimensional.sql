CREATE TABLE `dim_pacientes` (
  `id` integer PRIMARY KEY,
  `raca` varchar(255),
  `genero` varchar(255),
  `data_nascimento` datetime
);

CREATE TABLE `dim_faixa_etaria` (
  `id` integer PRIMARY KEY,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `fato_diagnostico` (
  `id` integer PRIMARY KEY,
  `internacao_id` integer NOT NULL,
  `codigo_problema` varchar(255) NOT NULL,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `fato_resultado_exame` (
  `id` integer PRIMARY KEY,
  `internacao_id` integer NOT NULL,
  `tipo_exame` varchar(255),
  `resultado` varchar(255)
);

CREATE TABLE `dim_medicamento` (
  `id` integer PRIMARY KEY,
  `nome` varchar(255) NOT NULL,
  `substancia` varchar(255) NOT NULL
);

CREATE TABLE `fato_administracao_medicamento` (
  `id` integer PRIMARY KEY,
  `internacao_id` integer NOT NULL,
  `medicamento_id` integer NOT NULL,
  `data_administracao` datetime
);

CREATE TABLE `dim_pagamento` (
  `id` integer PRIMARY KEY,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `dim_especialidade_medica` (
  `id` integer PRIMARY KEY,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `dim_tipo_internacao` (
  `id` integer PRIMARY KEY,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `dim_origem` (
  `id` integer PRIMARY KEY,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `dim_destino` (
  `id` integer PRIMARY KEY,
  `descricao` varchar(255) NOT NULL
);

CREATE TABLE `fato_internacoes` (
  `id` integer PRIMARY KEY,
  `paciente_id` integer NOT NULL,
  `dim_faixa_etaria_id` integer NOT NULL,
  `tipo_internacao_id` integer NOT NULL,
  `destino_id` integer NOT NULL,
  `origem_id` integer NOT NULL,
  `peso_paciente` decimal,
  `qtd_diagnosticos` integer NOT NULL,
  `tempo_internacao` integer NOT NULL,
  `qtd_exames_lab` integer NOT NULL,
  `qtd_procedimentos` integer NOT NULL,
  `qtd_emergencias` integer NOT NULL,
  `qtd_internacoes_anteriores` integer NOT NULL,
  `qtd_internacoes_ambulatoriais_anteriores` integer NOT NULL,
  `qtd_medicamentos` integer NOT NULL,
  `uso_medicamento_diabetes` boolean,
  `readmissao` boolean,
  `data_entrada` datetime,
  `data_saida` datetime,
  `pagamento_id` integer NOT NULL,
  `especialidade_medica_id` integer NOT NULL
);

ALTER TABLE `fato_diagnostico` ADD FOREIGN KEY (`internacao_id`) REFERENCES `fato_internacoes` (`id`);

ALTER TABLE `fato_resultado_exame` ADD FOREIGN KEY (`internacao_id`) REFERENCES `fato_internacoes` (`id`);

ALTER TABLE `fato_administracao_medicamento` ADD FOREIGN KEY (`medicamento_id`) REFERENCES `dim_medicamento` (`id`);

ALTER TABLE `fato_administracao_medicamento` ADD FOREIGN KEY (`internacao_id`) REFERENCES `fato_internacoes` (`id`);

ALTER TABLE `fato_internacoes` ADD FOREIGN KEY (`dim_faixa_etaria_id`) REFERENCES `dim_faixa_etaria` (`id`);

ALTER TABLE `fato_internacoes` ADD FOREIGN KEY (`paciente_id`) REFERENCES `dim_pacientes` (`id`);

ALTER TABLE `fato_internacoes` ADD FOREIGN KEY (`tipo_internacao_id`) REFERENCES `dim_tipo_internacao` (`id`);

ALTER TABLE `fato_internacoes` ADD FOREIGN KEY (`origem_id`) REFERENCES `dim_origem` (`id`);

ALTER TABLE `fato_internacoes` ADD FOREIGN KEY (`destino_id`) REFERENCES `dim_destino` (`id`);

ALTER TABLE `fato_internacoes` ADD FOREIGN KEY (`pagamento_id`) REFERENCES `dim_pagamento` (`id`);

ALTER TABLE `fato_internacoes` ADD FOREIGN KEY (`especialidade_medica_id`) REFERENCES `dim_especialidade_medica` (`id`);
