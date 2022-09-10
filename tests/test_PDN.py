import os
from parsing.PDN import PDNReader, PDNWriter


def test_parse_PDN_string_success():
    pdn_string = '[Event "Casual Game"]\n' + \
                 '[Site "https://itsyourturn.com"]\n' + \
                 '[Date "2019.11.26"\n' + \
                 '[Round "*"]\n' + \
                 '[White "Jubai"]\n ' + \
                 '[Black "windycity"]\n' + \
                 '[Result "1-0"]\n' + \
                 '[Ply "111"]\n' + \
                 '\n' + \
                 '1. 10-15 23-18 2. 7-10 22-17 3. 15-22 25-18 4. 11-15 \n' + \
                 '18-11 5. 8-15 24-20 6. 4-8 27-23 7. 9-13 20-16 8. \n' + \
                 '13-22 26-17 9. 12-19-26 30-23 10. 3-7 23-19 11. 15-24 \n' + \
                 '28-19 12. 7-11 17-14 13. 10-17 21-14 14. 2-7 32-27 \n' + \
                 '15. 8-12 29-25 16. 6-9 31-26 17. 9-18 19-15 18. 7-10 \n' + \
                 '15-8 19. 5-9 26-22 20. 10-15 22-17 21. 1-6 17-14 22. \n' + \
                 '9-13 14-10 23. 6-9 8-3 24. 15-19 3-7 25. 19-23 27-24 \n' + \
                 '26. 23-27 24-20 27. 13-17 25-21 28. 17-22 21-17 29. \n' + \
                 '18-23 17-13 30. 9-14 10-6 31. 14-17 6-2 32. 23-26 \n' + \
                 '7-10 33. 22-25 10-14 34. 17-21 14-18 35. 26-31 13-9 \n' + \
                 '36. 25-30 18-22 37. 27-32 9-5 38. 30-26 22-18 39. \n' + \
                 '26-23 18-27 40. 32-23 5-1 41. 21-25 2-7 42. 25-30 \n' + \
                 '7-10 43. 31-26 10-15 44. 26-31 1-6 45. 30-25 6-9 \n' + \
                 '46. 23-26 9-14 47. 26-22 15-19 48. 25-21 20-16 \n' + \
                 '49. 22-17 14-18 50. 17-22 18-25 51. 21-30 16-11 \n' + \
                 '52. 31-26 11-7 53. 26-23 19-26 54. 30-23 7-3 55. \n' + \
                 '23-18 3-8 56. 18-15 1-0\n'
    reader = PDNReader.from_string(pdn_string)
    assert reader.PDNs[0].event == "Casual Game"
    assert reader.PDNs[0].date == "2019.11.26"
    assert reader.PDNs[0].white == "Jubai"
    assert reader.PDNs[0].black == "windycity"
    assert reader.PDNs[0].result == "1-0"
    assert reader.PDNs[0].fen == '1. 10-15 23-18 2. 7-10 22-17 3. 15-22 ' + \
                                 '25-18 4. 11-15 18-11 5. 8-15 24-20 6. ' + \
                                 '4-8 27-23 7. 9-13 20-16 8. 13-22 26-17 ' + \
                                 '9. 12-19-26 30-23 10. 3-7 23-19 11. ' + \
                                 '15-24 28-19 12. 7-11 17-14 13. 10-17 ' + \
                                 '21-14 14. 2-7 32-27 15. 8-12 29-25 ' + \
                                 '16. 6-9 31-26 17. 9-18 19-15 18. 7-10 ' + \
                                 '15-8 19. 5-9 26-22 20. 10-15 22-17 ' + \
                                 '21. 1-6 17-14 22. 9-13 14-10 23. 6-9 ' + \
                                 '8-3 24. 15-19 3-7 25. 19-23 27-24 ' + \
                                 '26. 23-27 24-20 27. 13-17 25-21 28. ' + \
                                 '17-22 21-17 29. 18-23 17-13 30. 9-14 ' + \
                                 '10-6 31. 14-17 6-2 32. 23-26 7-10 ' + \
                                 '33. 22-25 10-14 34. 17-21 14-18 35. ' + \
                                 '26-31 13-9 36. 25-30 18-22 37. 27-32 ' + \
                                 '9-5 38. 30-26 22-18 39. 26-23 18-27 ' + \
                                 '40. 32-23 5-1 41. 21-25 2-7 42. 25-30 ' + \
                                 '7-10 43. 31-26 10-15 44. 26-31 1-6 45. ' + \
                                 '30-25 6-9 46. 23-26 9-14 47. 26-22 ' + \
                                 '15-19 48. 25-21 20-16 49. 22-17 14-18 ' + \
                                 '50. 17-22 18-25 51. 21-30 16-11 ' + \
                                 '52. 31-26 11-7 53. 26-23 19-26 54. ' + \
                                 '30-23 7-3 55. 23-18 3-8 56. 18-15 1-0'


def test_parse_PDN_file_success():
    pdn_file = os.path.join('training', 'OCA_2.0.pdn')
    reader = PDNReader.from_file(pdn_file)
    assert len(reader.PDNs) == 22621
    assert reader.PDNs[22620].event == "German Open 2004"


def test_write_PDN_file_success(tmp_path):
    pdn_filepath = os.path.join(tmp_path, "sample.pdn")
    event = "German Open 2004"
    date = "2004-05-01"
    rnd = ""
    black = "Morgan, John"
    white = "Pawlek, Dennis"
    site = "Reutlingen"
    result = "1/2-1/2"
    fen = "1. 11-15 22-17 2. 15-19 24x15 3. 10x19 23x16 4. 12x19 25-22 " + \
          "5. 7-10 27-24 6. 10-15 17-13 7. 9-14 29-25 8. 6-10 22-17 9. " + \
          "1-6 26-23 10. 19x26 30x23 11. 8-11 24-19 12. 15x24 28x19 13. " + \
          "3-7 25-22 14. 11-15 32-28 15. 15x24 28x19 16. 7-11 19-16 17. " + \
          "11x20 23-19 18. 14-18 22x15 19. 4-8 31-27 20. 5-9 27-23 21. " + \
          "9-14 19-16 22. 10x19x26 17x10x1 1/2-1/2"
    PDNWriter.to_file(pdn_filepath, event, site, date, rnd, black, white, 
                      result, fen)
    with open(pdn_filepath) as f1:
        with open(os.path.join('training', 'german_open_2004.pdn')) as f2:
            assert f1.readlines() == f2.readlines()


def test_write_PDN_string_success():
    event = "German Open 2004"
    site = "Reutlingen"
    date = "2004-05-01"
    rnd = ""
    black = "Morgan, John"
    white = "Pawlek, Dennis"
    result = "1/2-1/2"
    fen = "1. 11-15 22-17 2. 15-19 24x15 3. 10x19 23x16 4. 12x19 25-22 5. " + \
          "7-10 27-24 6. 10-15 17-13 7. 9-14 29-25 8. 6-10 22-17 9. " + \
          "1-6 26-23 10. 19x26 30x23 11. 8-11 24-19 12. 15x24 28x19 " + \
          "13. 3-7 25-22 14. 11-15 32-28 15. 15x24 28x19 16. 7-11 " + \
          "19-16 17. 11x20 23-19 18. 14-18 22x15 19. 4-8 31-27 20. " + \
          "5-9 27-23 21. 9-14 19-16 22. 10x19x26 17x10x1 1/2-1/2"
    pdn = PDNWriter.to_string(event, site, date, rnd, black, white, result,
                              fen)
    assert pdn == '[Event "German Open 2004"]\n' + \
                  '[Date "2004-05-01"]\n' + \
                  '[Black "Morgan, John"]\n' + \
                  '[White "Pawlek, Dennis"]\n' + \
                  '[Site "Reutlingen"]\n' + \
                  '[Result "1/2-1/2"]\n' + \
                  '1. 11-15 22-17 2. 15-19 24x15 3. 10x19 23x16 4. 12x19 25-22 5. 7-10 27-24 6.\n' + \
                  '10-15 17-13 7. 9-14 29-25 8. 6-10 22-17 9. 1-6 26-23 10. 19x26 30x23 11. 8-11\n' + \
                  '24-19 12. 15x24 28x19 13. 3-7 25-22 14. 11-15 32-28 15. 15x24 28x19 16. 7-11\n' + \
                  '19-16 17. 11x20 23-19 18. 14-18 22x15 19. 4-8 31-27 20. 5-9 27-23 21. 9-14\n' + \
                  '19-16 22. 10x19x26 17x10x1 1/2-1/2\n'
