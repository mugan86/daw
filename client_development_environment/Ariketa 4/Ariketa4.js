function konprobatu(pasahitza, pasahitzar)
{
    if (pasahitza == pasahitzar)
        return true;
    else
        return false;

}
function luzera(pasahitza)
{
	/*
    Hemen errorea zegoen, > jarrita zegoen >= beharrean
    */
    if (String(pasahitza).length >= 6)
        return true;
    else
        return false;
}