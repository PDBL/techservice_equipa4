

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