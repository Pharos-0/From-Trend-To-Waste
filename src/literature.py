"""External facts used in the report — each with its source, registered in the claims register."""
from .utils import register_claim

LITERATURE = {
    "lit_unep_ghg": ("Textile industry share of global greenhouse-gas emissions (UNEP)", "2-8%",
                     "https://www.unep.org/news-and-stories/press-release/un-alliance-sustainable-fashion-addresses-damage-fast-fashion"),
    "lit_emf_truck": ("Textiles landfilled or burned (Ellen MacArthur Foundation, A New Textiles Economy, 2017)",
                      "the equivalent of one garbage truck every second",
                      "https://www.ellenmacarthurfoundation.org/news/one-garbage-truck-of-textiles-wasted-every-second-report-creates-vision-for-change"),
    "lit_emf_recycle": ("Clothing remade into new clothing (Ellen MacArthur Foundation, 2017)", "less than 1%",
                        "https://www.ellenmacarthurfoundation.org/news/one-garbage-truck-of-textiles-wasted-every-second-report-creates-vision-for-change"),
    "lit_wrap_life": ("Average UK garment lifetime (WRAP)", "2.2 years (2012); 3.3 years (later update)",
                      "https://www.wrap.ngo/resources/report/valuing-our-clothes-true-cost-how-we-design-use-and-dispose-clothing-uk-2012"),
    "lit_wrap_co2": ("UK clothing whole-life carbon footprint per tonne (WRAP 2017)", "23.2 t CO2e per tonne (2016)",
                     "https://www.wrap.ngo/sites/default/files/2020-10/WRAP-valuing-our-clothes-the-cost-of-uk-fashion_WRAP.pdf"),
}


URL = {k: src for k, (_, _, src) in LITERATURE.items()}

# The report's reference list, in IEEE style. The report template cites them as [@key]; src/build_report.py numbers the
# cited ones in order of first appearance and lists only those. Every entry was checked against the publisher's or an
# index's record (title, authors, venue, volume, pages).
REFERENCES = {
    "caro2015": ("F. Caro and V. Martínez-de-Albéniz, \"Fast fashion: Business model overview and research opportunities,\" "
                 "in *Retail Supply Chain Management*, 2nd ed., N. Agrawal and S. A. Smith, Eds. Boston, MA, USA: Springer, "
                 "2015, pp. 237–264, doi: 10.1007/978-1-4899-7562-1_9."),
    "niinimaki2020": ("K. Niinimäki, G. Peters, H. Dahlbo, P. Perry, T. Rissanen, and A. Gwilt, \"The environmental price of "
                      "fast fashion,\" *Nat. Rev. Earth Environ.*, vol. 1, pp. 189–200, 2020, doi: 10.1038/s43017-020-0039-9."),
    "unep2019": ("UN Environment Programme, \"UN Alliance For Sustainable Fashion addresses damage of 'fast fashion',\" "
                 f"press release, Nairobi, Kenya, Mar. 14, 2019. [Online]. Available: {URL['lit_unep_ghg']}"),
    "emf2017": ("Ellen MacArthur Foundation, \"A new textiles economy: Redesigning fashion's future,\" 2017. [Online]. "
                f"Available: {URL['lit_emf_truck']}"),
    "wrap2012": ("WRAP, \"Valuing our clothes: The true cost of how we design, use and dispose of clothing in the UK,\" "
                 f"Banbury, U.K., 2012. [Online]. Available: {URL['lit_wrap_life']}"),
    "wrap2017": ("WRAP, \"Valuing our clothes: The cost of UK fashion,\" Banbury, U.K., 2017. [Online]. Available: "
                 f"{URL['lit_wrap_co2']}"),
    "fisher1996": ("M. Fisher and A. Raman, \"Reducing the cost of demand uncertainty through accurate response to early "
                   "sales,\" *Oper. Res.*, vol. 44, no. 1, pp. 87–99, 1996, doi: 10.1287/opre.44.1.87."),
    "smith1998": ("S. A. Smith and D. D. Achabal, \"Clearance pricing and inventory policies for retail chains,\" "
                  "*Manage. Sci.*, vol. 44, no. 3, pp. 285–300, 1998, doi: 10.1287/mnsc.44.3.285."),
    "caro2012": ("F. Caro and J. Gallien, \"Clearance pricing optimization for a fast-fashion retailer,\" *Oper. Res.*, "
                 "vol. 60, no. 6, pp. 1404–1422, 2012, doi: 10.1287/opre.1120.1102."),
    "skenderi2022": ("G. Skenderi, C. Joppi, M. Denitto, B. Scarpa, and M. Cristani, \"The multi-modal universe of "
                     "fast-fashion: The Visuelle 2.0 benchmark,\" in *Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. "
                     "Workshops (CVPRW)*, 2022, pp. 2240–2245, doi: 10.1109/CVPRW56347.2022.00245."),
    "skenderi2024": ("G. Skenderi, C. Joppi, M. Denitto, and M. Cristani, \"Well googled is half done: Multimodal forecasting "
                     "of new fashion product sales with image-based Google Trends,\" *J. Forecasting*, vol. 43, no. 6, "
                     "pp. 1982–1997, 2024, doi: 10.1002/for.3104."),
    "visuelle": ("Humatics Lab, University of Verona, \"VISUELLE 2.0\" (dataset; real data from Nuna Lie). [Online]. "
                 "Available: https://humaticslab.github.io/forecasting/visuelle"),
    "zhang2025": ("Y. Zhang, F. Wang, C. Lin, and G. T. M. Hult, \"Assessing fast fashion overstock through "
                  "time-to-peak-sales,\" *J. Retailing*, vol. 101, no. 3, pp. 431–453, 2025. [Online]. Available: "
                  "https://www.sciencedirect.com/science/article/abs/pii/S0022435925000351"),
    "fader2005": ("P. S. Fader, B. G. S. Hardie, and K. L. Lee, \"RFM and CLV: Using iso-value curves for customer base "
                  "analysis,\" *J. Marketing Res.*, vol. 42, no. 4, pp. 415–430, 2005, doi: 10.1509/jmkr.2005.42.4.415."),
    "green1990": ("P. E. Green and V. Srinivasan, \"Conjoint analysis in marketing: New developments with implications "
                  "for research and practice,\" *J. Marketing*, vol. 54, no. 4, pp. 3–19, 1990."),
    "rousseeuw1987": ("P. J. Rousseeuw, \"Silhouettes: A graphical aid to the interpretation and validation of cluster "
                      "analysis,\" *J. Comput. Appl. Math.*, vol. 20, pp. 53–65, 1987, doi: 10.1016/0377-0427(87)90125-7."),
    "friedman2001": ("J. H. Friedman, \"Greedy function approximation: A gradient boosting machine,\" *Ann. Statist.*, "
                     "vol. 29, no. 5, pp. 1189–1232, 2001, doi: 10.1214/aos/1013203451."),
    "hyndman2006": ("R. J. Hyndman and A. B. Koehler, \"Another look at measures of forecast accuracy,\" *Int. J. "
                    "Forecasting*, vol. 22, no. 4, pp. 679–688, 2006, doi: 10.1016/j.ijforecast.2006.03.001."),
    "pedregosa2011": ("F. Pedregosa et al., \"Scikit-learn: Machine learning in Python,\" *J. Mach. Learn. Res.*, "
                      "vol. 12, pp. 2825–2830, 2011."),
    "upc2022": ("Universitat Politècnica de Catalunya, \"Reusing 1 kg of clothing saves 25 kg of CO2, according to a study "
                "by INTEXTER,\" 2022. [Online]. Available: https://www.upc.edu/en/press-room/news/"
                "reusing-1-kg-of-clothing-saves-25-kg-of-co2-according-to-a-study-by-intexter"),
}


def main():
    for k, (claim, value, src) in LITERATURE.items():
        register_claim(k, claim, value, src)


if __name__ == "__main__":
    main()
