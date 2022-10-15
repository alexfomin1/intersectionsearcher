# cases
case1 = {
    'casename': 'a in [a1, a2] and b in [b3, b8]',
    'conditions': [
        {'a': ['a1', 'a2']},
        {'b': ['b3', 'b8']},
    ]
}

case2 = {
    'casename': 'a not in [a1, a2] and b in [b3, b8]',
    'conditions': [
        {'a': {'a1', 'a2'}},
        {'b': ['b3', 'b8']},
    ]
}

case3 = {
    'casename': 'a in [a3, a1] and b not in [b8]',
    'conditions': [
        {'a': ['a3', 'a1']},
        {'b': {'b8'}},
    ]
}

case4 = {
    'casename': 'a not in [a5, a6] and b not in [b9, b11]',
    'conditions': [
        {'a': {'a5', 'a6'}},
        {'b': {'b9', 'b11'}},
    ]
}


# requests
req0 = {}
req1 = {'a': 'a0'}
req2 = {'a': 'a1'}
req3 = {'b': 'b3'}
req4 = {'a': 'a2', 'b': 'b3'}
req5 = {'a': 'a1', 'b': 'b8'}
req6 = {'a': 'a8', 'b': 'b8'}
req7 = {'a': 'a3', 'b': 'b3'}

# map of truth
request_response_true_map = [
    (req0, []),
    (req1, []),
    (req2, []),
    (req3, []),
    (req4, [case1['casename'], case4['casename']]),
    (req5, [case1['casename'], case4['casename']]),
    (req6, [case2['casename'], case4['casename']]),
    (req7, [case2['casename'], case3['casename'], case4['casename']])
]

'''
== ALGORITHM ==
1. Check length of request
2. Check every case's type of conditions
3.1. If dictionary -> not include
3.2. If list -> include
4. Form message: "a not in/in [condition] and b not in/in [condition]"
'''
class IntersectionSearcher:
    _cases = []

    def __init__(self, case_list):
        self._cases = case_list

    def process(self, request):
        if len(request) < 2:
            return []

        list_of_results = []
        for case in self._cases:
            '''
            = Example of case =
            {
            'casename': 'a not in [a5, a6] and b not in [b9, b11]',
            'conditions': [
                {'a': {'a5', 'a6'}},
                {'b': ['b9', 'b11']},
            ]
            }
            '''
            fl = True # flag for checking if we follow the conditions
            for condition in case['conditions']:
                '''
                = example of condition =
                {'a': {'a5', 'a6'}}
                '''
                for key, value in condition.items():
                    if isinstance(value, set) and request[key] not in value:
                        pass
                    elif isinstance(value, list) and request[key] in value:
                        pass
                    else:
                        fl = False
                        break
            if fl:
                list_of_results.append(case['casename'])
        return list_of_results

IS = IntersectionSearcher([case1, case2, case3, case4])


def test_0_empty_request():
    request, expected_response = request_response_true_map[0]
    response = IS.process(request)
    assert response == expected_response


def test_1_empty_request():
    request, expected_response = request_response_true_map[1]
    response = IS.process(request)
    assert response == expected_response


def test_2_empty_request():
    request, expected_response = request_response_true_map[2]
    response = IS.process(request)
    assert response == expected_response


def test_3_empty_request():
    request, expected_response = request_response_true_map[3]
    response = IS.process(request)
    assert response == expected_response


def test_4_empty_request():
    request, expected_response = request_response_true_map[4]
    response = IS.process(request)
    assert response == expected_response


def test_5_empty_request():
    request, expected_response = request_response_true_map[5]
    response = IS.process(request)
    assert response == expected_response


def test_6_empty_request():
    request, expected_response = request_response_true_map[6]
    response = IS.process(request)
    assert response == expected_response


def test_7_empty_request():
    request, expected_response = request_response_true_map[7]
    response = IS.process(request)
    assert response == expected_response
