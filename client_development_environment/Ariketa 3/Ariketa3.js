function gaindituta(zenbaki1, zenbaki2, zenbaki3)
{
    if (batazbestekoa(zenbaki1, zenbaki2, zenbaki3) >= 5)
    {
        return true;
    }
    else
    {
        return false;
    }

}

function batazbestekoa(zenbaki1, zenbaki2, zenbaki3)
{
    return (zenbaki1 + zenbaki2 + zenbaki3) / 3;
}