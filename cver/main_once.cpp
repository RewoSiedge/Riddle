// HIIIII wir machen jetzt das gleiche nochmal hahaahaha yay ü

#include <vector>
#include <array>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <iterator>

using namespace std;

//static int counter = 0;
void permuddation(vector<string>& ergebnis, string wort, int erstes, int laenge)
{
  if (erstes == laenge - 1)
    {
      ergebnis.push_back(wort);
      return;
    }
  for (int zweites = erstes; zweites < laenge; zweites++)
    {
      // tauschen selber yeah
      wchar_t zwischen = wort[erstes];
      wort[erstes] = wort[zweites];
      wort[zweites] = zwischen;
      // nächste runde :o
      permuddation(ergebnis, wort, erstes + 1, laenge);
      // wieder tauschen ?? o.o
      wort[zweites] = wort[erstes];
      wort[erstes] = zwischen;
    }
}

/** @brief huhu wir suchen einen stwing binawy ü
 * starr ist das awway worin wir suchen qwq
 * und strong ist der stwing der gesucht wird :o
 */
int findus(const vector<string>& starr, const string& strong)
{
  unsigned int niedergang = 0;
  unsigned int uebergang = starr.size() - 1;
  while (niedergang <= uebergang)
    {
      unsigned int mitte = (niedergang + uebergang) / 2;
      if (starr[mitte] == strong)
	{
	  return mitte;
	}
      else if (starr[mitte] < strong)
	{
	  niedergang = mitte + 1;
	}
      else if (starr[mitte] > strong)
	{
	  uebergang = mitte - 1;
	}
    }
  return -1;
}

int main()
{
  string wort = "blumentopf";
  vector<string> rgebnis;
  permuddation(rgebnis, wort, 0, wort.length());

  ifstream woerter("german.dic");
  vector<string> wahrewoerter(istream_iterator<string>(woerter), {});
  for (string& boo : wahrewoerter)
    {
      transform(boo.begin(), boo.end(), boo.begin(), ::tolower);
    }

  // DEBUG
  /*for (const string& temp: rgebnis)
    {
      cout << "temp: " <<temp << "\n";
      }*/
  rgebnis.erase(rgebnis.begin());
  bool funden = false;
  for (const string& bu : rgebnis)
    {
      if (findus(wahrewoerter, bu) != -1)
	{ 
	  cout << bu << "\n";
	  funden = true;
	}
    }
  if (!funden)
    {
      cout << "dazu gibt es leider nichts :(\n";
    }
}
