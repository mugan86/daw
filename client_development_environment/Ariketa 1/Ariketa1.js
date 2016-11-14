function faktoriala(zenbaki)
{
    var erantzuna = 1;
    for (i = 1; i <= zenbaki; i++)
    {
        erantzuna *= i;
    }
    return erantzuna;
}