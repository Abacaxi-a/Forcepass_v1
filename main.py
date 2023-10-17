from playwright.sync_api import sync_playwright

def force():
    with sync_playwright() as p:
        df = pd.read_csv('teste.csv',delimiter=';')
        guia = p.chromium.launch(headless=False)

        context = guia.new_context()
        page = context.new_page()

        page.goto('...')
        for i in range(0,9):
            try:
                time.sleep(1)
                page.fill('input[id="login-user_name"]',df['user'][i])
                time.sleep(1)
                page.fill('input[id="login-password"]',str(df['senha'][i]))
                page.locator('button[id="login-button"]').click()  
                a = 'o possivel acesso é',df['user'][i],', e a senha é',df['senha'][i]
            except:
                print('nenhum acesso encontrado, ou ja foi logado')
                break
        page.locator('xpath:/html/body/div[1]/div/div/section/div[2]/div[1]/div/div/label')

        time.sleep(5)
        print(a,flush=True)
        page.close()
force()