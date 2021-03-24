int main(void) {
    void copiaConteudo(FILE *arquivo, FILE *arquivo1);
    FILE *arquivo = fopen("tmp/exercicio.txt","r");
    if (arquivo == NULL)
    {
        printf ("Não foi possível abrir o arquivo");
        return 1;
    }

    FILE *arquivo1 = fopen("home/novo.txt","w");    
    copiaConteudo(arquivo,arquivo1);        
    fclose(arquivo);
    fclose(arquivo1);
    return 0;
}

void copiaConteudo(FILE *arquivo, FILE *arquivo1)
{
    string teste;
    teste = "Teste";
    char ler[100];
    while(fgets(ler,100,arquivo) != NULL)

    if (ler.find("Teste"))
    {
        fputs("0/",arquivo);    
    }
    else
    {
        fputs(ler, arquivo1);
    }
}