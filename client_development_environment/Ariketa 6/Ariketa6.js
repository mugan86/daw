function konprobatu(zenbaki)
{
    var digitoak;
    if (zenbaki > 0 && zenbaki < 10)
    {
        digitoak = 1;
    }
    else
        if (zenbaki >= 10 && zenbaki < 100)
        {
            digitoak = 2;
        }
        else
            if (zenbaki >= 100 && zenbaki < 1000)
            {
                digitoak = 3;
            }
            else
                {
                    digitoak = 0;
            }

    return digitoak;
}