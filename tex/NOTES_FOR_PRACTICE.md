# Введение

Спустя тридцать лет после появления первых коммерческих мобильных коммуникационных систем, беспроводная связь эволюционировала в обыкновенное удобство как газ или электричество. Экспоненциальный рост в мобильном трафике в течение последних трёх десятилетий привел к мас­штабному развертыванию беспроводных систем. Как следствие, ограничен­ный доступный РЧ­диапазон является объектом постоянного переиспользования и межканальной интерференции, что значительно ограничивает ём­кость сетей. Таким образом, было много различных предупреждений о грядущем «кризисе РЧ спектра» [1], так как требования к передачи мобильных данных данных продолжают расти, в то время как спектральная эффективность сетей насыщается, даже несмотря на введение новых стандартов и значительный технологический прогресс в этой области. По оценкам, к 2022году более 77 эксабайтов (10^60 байт) трафика будет передаваться через мобильные устройства каждый месяц (около одного зеттабайта в год) [2]. В середине прошлого десятилетия было предложено использование связи по видимому свету (VLC) в качестве потенциального решения для избежания«кризиса РЧ спектра».В течение прошлого десятилетия значительные усилия были направлены на изучение альтернативных частей электро­магнитного спектра, кото­рые потенциально смогут разгрузить бо́льшую часть трафика из загруженного РЧ диапазона. Было продемонстрировано использование миллиметровых волн в коммуникации в 28 ГГц диапазоне, а так же использование видимого и ИК света. Это особенно полезно, так как освещение – удобство, которое имеется практически в любой жилой среде и для которого существует готовая инфраструктура. Использование видимого света для высокоскоростных линий связи становится возможно из­за использования LED. В этом смысле концепт комбинирования функций освещения и коммуникации позволя­ет экономить энергию (и деньги) и сократить углеродный след. Во­первых,установка точек доступа является достаточно тривиальной задачей, так как можно переиспользовать уже существующую инфраструктуру с использованием готовых технологий, таких как связь по электросети (PLC) и питание через Ethernet (PoE). Во­вторых, так как освещение обычно работает в помещениях даже в течение светлого времени суток, дополнительное питание передатчиков будет незначительным. Помимо этого, видимый свет включает в себя сотни ТГц свободного канала, что на четыре порядка больше, чем полный РЧ спектр до 30 ГГц, включая миллиметровый спектр. Оптическое излучение, в общем, не интерферирует с другими радио волнами и не мешает работе чувствительного электрического оборудования. Таким образом, свет идеален для беспроводного покрытия в местах, чувствительных к электро­магнитному излучению (например, больницы, самолёты, топливно­химические и атомные электростанции и другие). Помимо этого, так как свет не может проникать через непрозрачные поверхности (стены), создается бо­лее высокий уровень безопасности соединения. Эта же особенность может быть использована для избежания интерференции между двумя соседними сетями.

# Основная часть

В качестве источника излучения был выбран ИК лазерный диодFPL1055T с длиной волны излучения 1550 нм, мощностью излучения в импульсном режиме 300 мВт, поперечной расходимостью 28◦и боковой расходимостью 15◦ [43]. Выбранный фотодиод – FDGA05 с пиковой длиной волны 1550 нм (регистрируемый диапазон длин волн 800-­1700 нм), фоточувствительностью 0.95 А/Вт, площадью активной области 0.196 мм^2 и материалом сенсора InGaAs [44]. Для моделирования оптической системы использовался пакет Zemax OpticStudio 21.1.2. Для фотодиода заданы размеры апертуры (взяты из документации), количество угловых и радиальных зон оставлены по умолчанию и необходимы для расчётов в симуляции. Положение фотодиода задаётся относительно круга с отверстием и соответствует положению фотодиода в корпусе.

Аналогично было проведено исследование зависимости оптической мощности на фотодиоде, при наличии собирающей линзы, от расстояния между фотодиодом и линзой. Очевидно, что наибольшая мощность достигается, когда фоточувствительная площадка находится на фокусном расстоянии от линзы. Помимо этого, было проведено исследование оптической мощности на фотоприёмнике от угла поворота источника излучения.

Пропускная способность фотодиода была рассчитана теоретически по данным производителя. Была собрана экспериментальная установка для измерения ёмкости фотодиода с целью определения реальной пропускной способности. Она состояла из векторного анализатора цепей, к которому были подсоединены ЛД и ФД через SMA разъемы. Из-за того, что фотодиод оказался не согласован по высоким частотам, в сверхвысокочастотный тракт сигнал не прошёл, в связи с чем измерение ёмкости не представляется возможным.

# Вывод

Результатом выпускной квалификационной работы являются модель оптической системы в программе Zemax OpticStudio. В ходе работы был про­веден обзор существующей коммерчески доступной компонентной базы, на примере производителя Thorlabs, выбран фотодетектор, построена модель оптической системы с ним,проведено исследование зависимости оптической мощности на нём в зависимости от различных параметров системы, был про­ведён эксперимент с целью рассчитать ширину полосу пропускания фотодиода.В ходе работы было показано, что возможно создание Li­Fi сети с ис­пользованием стандартных компонентов, что позволит увеличить скорость внедрения и популяризации технологии, инфракрасной длины волны для вос­ходящего сигнала, что является безопасным для человека, не мешает в освещении и позволяет увеличить мощность источника излучения для повыше­ния качества передаваемого сигнала и скорости передачи информации. Была построена модель оптической системы, которая позволяет исследовать зависимость оптической мощности, улавливаемой фоточувствительной площадкой фотоприёмника в зависимости от различных параметров системы – углы расходимости источника, угол поворота источника, расстояние между источником и приёмником, мощность источника.В дальнейшем работу можно продолжить: при использовании схемы согласования, возможно измерить ёмкость фотодиода и рассчитать его поло­су пропускания, исследовать возможность и целесообразность использования светофильтров и просветляющего покрытия на оптике (фокусирующая линза, защитное стекло фотоприёмника) для улучшения качества связи или уменьшения необходимой мощности излучения источника.

# Литература

1. Study on the future UK spectrum demand for terrestrial mobile broad­band applications : Rep. / Ofcom : 2013.—Jun.

2. Cisco Visual Networking Index: Global Mobile Data TrafficForecast Update, 2017–2022 : Rep. / Cisco : 2019.—Feb.—Access mode:https://s3.amazonaws.com/media.mediapost.com/uploads/CiscoForecast.pdf(online; accessed: May 28,2021).

3. 1­Gb/s Transmission Over a Phosphorescent White LED by UsingRate­Adaptive Discrete Multitone Modulation / A. M. Khalid, G. Cossu,R. Corsini et al. // IEEE Photonics Journal.—2012.—Oct.—Vol. 4, no. 5.—P. 1465–1473.

4. 3.4 Gbit/s visible optical wireless transmission based on RGB LED /G. Cossu, A. M. Khalid, P. Choudhury et al. //Optics Express.—2012.—Dec.—Vol. 20, no. 26.—P. B501.—Access mode:https://doi.org/10.1364/oe.20.00b501.

5. Azhar A., Tran T., O’Brien D. A Gigabit/s Indoor Wireless Transmis­sion Using MIMO­OFDM Visible­Light Communications // IEEE PhotonicsTechnology Letters.—2013.—Jan.—Vol. 31, no. 6.—P. 918–929.

6. Dimitrov S., Haas H. Information rate of ofdm­based optical wire­less communication systems with nonlinear distortion // Journal of LightwaveTechnology.—2013.—Vol. 31, no. 6.—P. 918–929.

7. VLC: Beyond Point­to­Point Communication / B. Harald, S. Nikola,T. Dobroslav et al. // IEEE Communications Magazine.—2014.

8. What is LiFi? / Harald Haas, Liang Yin, Yunlu Wang, Cheng Chen //J. Lightwave Technol.—2016.—Mar.—Vol. 34, no. 6.—P. 1533–1544.—Access mode:http://jlt.osa.org/abstract.cfm?URI=jlt­34­6­1533.

9. Haas Harald. Wireless data from every light bulb.—2011.—Jul.—Access mode:https://www.ted.com/talks/harald_haas_wireless_data_from_every_light_bulb(online; accessed: May28, 2021).

10. IEEE 802.15.7­2018 ­ IEEE Standard for Local and metropolitanarea networks–Part 15.7: Short­Range Optical Wireless Communications.—2018.—Access mode:https://standards.ieee.org/standard/802_15_7­2018.html(online; accessed: 2021­03­21).

11. High­speed visible light communications using multiple­resonantequalization / H. Le Minh, D. O’Brien, G. Faulkner et al. // IEEE PhotonicsTechnology Letters.—2008.—Vol. 20, no. 14.

12. Komine T., Haruyama S., Nakagawa M. Performance evaluation ofnarrowband OFDM on integrated system of power line communication andvisible light wireless communication // 1st International Symposium on Wire­less Pervasive Computing.—2006.—P. 1–6.

13. Komine T., Nakagawa M. Fundamental analysis for visible­light com­munication system using LED lights // IEEE Trans. Consum. Electron.—2004.—Vol. 50, no. 1.—P. 100–107.

14. Bian Rui, Tavakkolnia Iman, Haas Harald. 15.73 Gb/s Visible LightCommunication With Off­the­Shelf LEDs //Journal of Lightwave Technol­ogy.—2019.—May.—Vol. 37, no. 10.—P. 2418–2424.—Access mode:https://doi.org/10.1109/jlt.2019.2906464.

15. Four­color laser white illuminant demonstrating high color­renderingquality/A.Neumann,J.J.Wierer,W.Davisetal.//OpticsExpress.—2011.—Jul.—Vol. 19, no. S4.—P. A982.—Access mode:https://doi.org/10.1364/oe.19.00a982.

16. Hussein Ahmed Taha, Elmirghani Jaafar M. H. Mobile Multi­GigabitVisible Light Communication System in Realistic Indoor Environment //Journal of Lightwave Technology.—2015.—Aug.—Vol. 33, no. 15.—P. 3293–3307.—Access mode:https://doi.org/10.1109/jlt.2015.2439051.

17. HaberlinHeinrich. Photovoltaicssystemdesignandpractice.—Wiley,2014.—ISBN:9781119978381.—Access mode:http://rbdigital.oneclickdigital.com.

18. Photodiode Characteristics and Applications : Rep. /OSI Optoelectronics : 2006.—Access mode:http://www.osioptoelectronics.com/application­notes

19. Нойкин Ю.М., Махно П.В. Физические основы оптической свя­зи.—ФГАОУ ВО ”Южный федеральный университет2011.

20. Decoding methods in LED­to­smartphone bidirectional communica­tion for the IoT/ Alexis Duquel, Razvan Stanica, Herve Rivano, Adrien De­sportes // 2018 Global LIFI Congress (GLC).—IEEE, 2018.—Feb.—Accessmode:https://doi.org/10.23919/glc.2018.8319118.

21. Demonstration of A Visible Light Receiver Using Rolling­ShutterSmartphone Camera/ Tuan­Kiet TRAN, Huu­Thuan HUYNH, Duc­Phuc NGUYEN et al. // 2018 International Conference on Advanced Tech­nologies for Communications (ATC).—IEEE, 2018.—Oct.—Access mode:https://doi.org/10.1109/atc.2018.8587521.

22. Artūras Žukauskas, Michael Shur, Remis Gaska. Introduction to solid­state lighting.—New York : J. Wiley, 2002.—ISBN:9780471215745.

23. Human electroretinogram responses to video displays, fluorescentlighting, and other high frequency sources / S. M. Berman, D. S. Greehouse,I. L. Bailey et al. // Optom. Vis. Sci.—1991.—Aug.—Vol. 68, no. 8.—P. 645–662.

24. Wireless high ­speed data transmission with phosphorescent white ­light LEDs / J. Grubor, S. C. J. Lee, K.­D. Langer et al. // 33rd Eur. Conf. Exhib.Opt. Commun.—Post­Deadline Papers.—2007.—Sep.—P. 1–2.

25. Park S. Information broadcasting system based on visible light sign­board // Wireless Opt. Commun.—2007.—P. 311–313.

26. Minh H. L. High­speed visible light communications using multiple­resonantequalization//IEEEPhoton. Technol. Lett.—2008.—Jul.—Vol.20,no. 14.—P. 1243–1245.

27. Vucic J. 125 Mbit/s over 5 m wireless distance by use of OOK­ModulatedphosphorescentwhiteLEDs//35thECOC.—2009.—Sep.—P.1–2.

28. Vucic J. 230 Mbit/s via a wireless visible­light link based on OOKmodulation of phosphorescent white LEDs // Conf. OFC/NFOEC.—2010.—Mar.—P. 1–3
