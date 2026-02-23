```markdown
# 🔐 Comunicação Segura com Sockets UDP

## 📌 Descrição

Este projeto implementa um sistema de comunicação segura entre **cliente e servidor utilizando o protocolo UDP em Python**, garantindo:

- 🔒 **Confidencialidade** dos dados com criptografia AES-256 (modo CBC)
- 🛡 **Integridade** da mensagem com hash SHA-256

A comunicação utiliza uma **chave simétrica pré-compartilhada de 32 bytes**, garantindo segurança na troca de mensagens.

---

# 🧠 Conceitos Utilizados

## 🔐 Confidencialidade – AES-256 (CBC)

- Algoritmo: AES (Advanced Encryption Standard)
- Tamanho da chave: 256 bits (32 bytes)
- Modo de operação: CBC (Cipher Block Chaining)
- Vetor de Inicialização (IV): 16 bytes gerados aleatoriamente
- Padding: PKCS7

O modo CBC exige um IV diferente para cada mensagem enviada, evitando reutilização e aumentando a segurança.

---

## 🛡 Integridade – SHA-256

O algoritmo SHA-256 é utilizado para garantir que a mensagem não foi alterada durante o envio.

### Processo:

O cliente:

1. Calcula o hash do conteúdo criptografado (ciphertext).
2. Envia o hash junto com os dados.

O servidor:

1. Recalcula o hash do ciphertext recebido.
2. Compara com o hash enviado.
3. Descarta a mensagem caso os valores sejam diferentes.

---

# 📁 Estrutura do Projeto
```

SocketsSeguros/
│
├── servidor.py
├── cliente.py
└── README.md

````

---

# ⚙️ Pré-requisitos

- Python 3 instalado
- Biblioteca `cryptography`

Instale a biblioteca com o comando:

```bash
pip install cryptography
````

---

# ▶️ Como Executar

## 1️⃣ Abra dois terminais

Certifique-se de estar dentro da pasta onde estão os arquivos `servidor.py` e `cliente.py`.

---

## 2️⃣ Execute o Servidor

No primeiro terminal:

```bash
python servidor.py
```

Saída esperada:

```
Servidor seguro está pronto para receber...
```

O servidor ficará aguardando mensagens.

---

## 3️⃣ Execute o Cliente

No segundo terminal:

```bash
python cliente.py
```

Digite a mensagem quando solicitado.

---

# 🧪 Exemplo de Execução

Mensagem digitada no cliente:

```
Olá professor
```

Saída exibida no servidor:

```
Mensagem recebida (texto claro): Olá professor
```

---

# 👨‍💻 Autor

David da Silva dos Reis
Curso: Análise e Desenvolvimento de Sistemas
