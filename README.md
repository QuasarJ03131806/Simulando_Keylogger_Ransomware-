# Projeto de Simulação de Malware (Educacional)

Este projeto foi desenvolvido como parte de um desafio educacional para compreender o funcionamento de malwares (Ransomware e Keylogger) e, principalmente, como se defender deles.

**AVISO LEGAL:** Este código é estritamente para fins educacionais. O uso dessas ferramentas em sistemas sem autorização explícita é ilegal e antiético.

## Estrutura do Projeto

- `ransomware/`: Contém o script de simulação de Ransomware.
  - `ransomware.pyw`: Script principal (extensão .pyw para execução furtiva no Windows).
  - `target_folder/`: Pasta com arquivos de teste para serem criptografados.
- `keylogger/`: Contém o script de simulação de Keylogger.
  - `keylogger.pyw`: Script principal (extensão .pyw para execução furtiva no Windows).

## Como Executar

### Pré-requisitos

Você precisará do Python instalado e das seguintes bibliotecas:

```bash
pip install cryptography pynput
```

**Configuração de E-mail:**
Para que o envio de e-mails funcione, você deve editar os arquivos `ransomware.pyw` e `keylogger.pyw` e substituir `YOUR_APP_PASSWORD_HERE` pela sua "Senha de Aplicativo" (App Password) do Gmail. O e-mail de destino já está configurado como `upperprovedor@gmail.com`.

### Ransomware Simulado

1. Navegue até a pasta `ransomware`.
2. Execute o script: `python ransomware.pyw` (ou clique duas vezes no Windows).
3. Escolha a opção **1** para gerar uma chave. **A chave será enviada para o e-mail configurado.**
4. Escolha a opção **2** para criptografar os arquivos na pasta `target_folder`.
5. Verifique que os arquivos agora estão ilegíveis.
6. Escolha a opção **3** para descriptografar e recuperar os arquivos.

### Keylogger Simulado

1. Navegue até a pasta `keylogger`.
2. Execute o script: `python keylogger.pyw` (ou clique duas vezes no Windows).
   - **Nota:** Como é um arquivo `.pyw`, nenhuma janela abrirá. O script rodará em segundo plano.
3. Digite qualquer coisa em qualquer janela.
4. A cada 60 segundos (configurável), o script enviará o conteúdo digitado para o e-mail `upperprovedor@gmail.com` com o assunto "Keylogger Report".
5. Para parar o keylogger, você precisará finalizar o processo `pythonw.exe` (ou `python`) no Gerenciador de Tarefas.

## Reflexão sobre Defesa e Prevenção

### Defesa contra Ransomware

1.  **Backups Regulares:** A defesa mais eficaz. Mantenha backups offline (desconectados da rede) para que não sejam criptografados também.
2.  **Atualizações de Software:** Mantenha o sistema operacional e softwares atualizados para corrigir vulnerabilidades exploradas por malwares.
3.  **Filtragem de E-mail:** Muitos ransomwares chegam via phishing. Treinamento de usuários para não clicar em links suspeitos é crucial.
4.  **Controle de Permissões:** Usuários não devem ter permissões de administrador por padrão.
5.  **Monitoramento de Rede:** Detectar tráfego anômalo ou conexões com servidores de comando e controle (C2).

### Defesa contra Keyloggers

1.  **Antivírus/Antimalware:** Ferramentas de segurança modernas detectam assinaturas de keyloggers conhecidos e comportamentos suspeitos (heurística).
2.  **Teclados Virtuais:** Para digitar senhas sensíveis (como em bancos), o uso de teclados virtuais pode mitigar keyloggers de hardware ou software simples.
3.  **Autenticação de Dois Fatores (2FA):** Mesmo que a senha seja capturada, o atacante não conseguirá acessar a conta sem o segundo fator.
4.  **Firewall:** Bloquear conexões de saída não autorizadas pode impedir que o keylogger envie os dados capturados para o atacante.
5.  **Criptografia de Teclado:** Alguns softwares de segurança criptografam a entrada do teclado no nível do driver.

## Conclusão

Entender como o ataque funciona é o primeiro passo para construir uma defesa robusta. Este projeto demonstrou a simplicidade técnica de alguns malwares, reforçando a necessidade de vigilância constante e boas práticas de segurança cibernética.
