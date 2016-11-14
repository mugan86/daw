function gehiketa(zenbaki1, zenbaki2)
{
    return zenbaki1 + zenbaki2;
}
function kenketa(zenbaki1, zenbaki2) {
    return zenbaki1 - zenbaki2;
}
function biderketa(zenbaki1, zenbaki2) {
    return zenbaki1 * zenbaki2;
}
function zatiketa(zenbaki1, zenbaki2) {
    return zenbaki1 / zenbaki2;
}
function konparaketa(zenbaki1, zenbaki2)
{
    if (zenbaki1 > zenbaki2)
    {
        return zenbaki1 + "+" + zenbaki2 + "=" + gehiketa(zenbaki1, zenbaki2) + " " + zenbaki1 + "-" + zenbaki2 + "=" + kenketa(zenbaki1, zenbaki2);
    }
    else {
        return zenbaki1 + "*" + zenbaki2 + "=" + biderketa(zenbaki1, zenbaki2) + " " + zenbaki1 + "/" + zenbaki2 + "=" + zatiketa(zenbaki1, zenbaki2);
    }
}