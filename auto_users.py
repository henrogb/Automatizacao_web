import time
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

login_page = "https://admin.thexpos.net/users"

usuario = 'HENRO.SILVA'
senha = '@Fr33d0m03'

def login_maker(nome_usuario):    
    nome = new_user.split(" ")
    primeiro = nome[0]
    ultimo = nome[-1]
    log = f"{primeiro}.{ultimo}"
    return log



navegador = webdriver.Chrome()

navegador.get(login_page)

navegador.maximize_window()

wait = WebDriverWait(navegador, 10)

login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[placeholder='Insira seu usuário']")))
login.send_keys(usuario)

password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[placeholder='Insira sua senha']")))
password.send_keys(senha)


botao_login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'po-button')))
botao_login.click()

produto = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.po-menu-item[aria-label='Usuários']")))
produto.click()



df = pd.read_excel("../usuarios.xlsx")

for index, row in df.iterrows():
    new_user = row["nome"]
    aniv = row["aniversario"] 
    cpf = str(row["cpf"]).zfill(11)
    celular = str(row["celular"])
    email = row["email"]
    senha_padrao = "Master@2025"

    # Criar usuário
    novo_usuario = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@class='po-button' and @p-kind='primary']//span[normalize-space(text())='Novo Usuário']"))
    )
    novo_usuario.click()

    nome_u = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='name']")))
    nome_u.send_keys(new_user)

    logs = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='hidden']")))
    login_gen = login_maker(new_user)
    logs.send_keys(login_gen)

    birth_date = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='datepicker']")))
    birth_date.send_keys(aniv)

    apelido = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='nickName']")))
    apelido.send_keys(new_user)

    dropdown = navegador.find_element(By.CSS_SELECTOR, "select.po-select[name='select']")
    select = Select(dropdown)
    select.select_by_visible_text("Cpf")

    i_cpf = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='documentNumber']")))
    i_cpf.send_keys(cpf)

    i_celular = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='phone']")))
    i_celular.send_keys(celular)

    i_email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='email']")))
    navegador.execute_script("""
    arguments[0].value = arguments[1];
    arguments[0].dispatchEvent(new Event('input'));
    arguments[0].dispatchEvent(new Event('change'));
    """, i_email, email)
    i_email.send_keys(Keys.TAB)

    senha_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='password']")))
    senha_input.send_keys(senha_padrao)

    confirme_senha = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.po-input[name='confirmNewPassword']")))
    confirme_senha.send_keys(senha_padrao)

    elemento = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.po-input-icon-right[aria-label='Perfil']")))
    navegador.execute_script("arguments[0].scrollIntoView(true);", elemento)
    elemento.click()

    caixa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.po-item-list[aria-label='Caixa']")))
    caixa.click()

    salvar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'po-button')]//span[normalize-space(text())='Salvar']")))
    salvar.click()
    
    toaster = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "po-toaster.po-toaster-success"))
    )


    mensagem = toaster.find_element(By.CLASS_NAME, "po-toaster-message").text
    print("Mensagem do toast:", mensagem)


    botao_concluido = toaster.find_element(By.CLASS_NAME, "po-toaster-button-close")
    botao_concluido.click()

    # pequena pausa entre cadastros
    time.sleep(2)

print("usuários cadastrados com sucesso!!")
time.sleep(20)
navegador.quit()