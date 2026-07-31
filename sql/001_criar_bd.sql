

-- ====================================

use techservice_equipa4;

drop table if exists prioridade_os;

create table prioridade_os (

id_prioridade INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50),
descricao VARCHAR(255),
nivel INT NOT NULL
	CHECK (nivel in (1, 2, 3)),
    
ativo TINYINT NOT NULL DEFAULT 1
	CHECK (ativo IN (0, 1))
    );


-- Script para ligar as bases de dados --

use techservice_equipa4;

ALTER TABLE techservice_equipa4.ordens_servico
ADD CONSTRAINT fk_ordens_servico_prioridade_os
FOREIGN KEY (id_prioridade)
REFERENCES techservice_equipa4.prioridade_os(id_prioridade)
ON DELETE SET NULL
ON UPDATE CASCADE;

----------------------------------------------------------