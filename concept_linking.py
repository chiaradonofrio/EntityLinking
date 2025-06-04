from CMA import *
import ast

def loadRAGResults(filename):
    try:
        with open(filename, 'r') as file:
            data = []
            for line in file:
                line = line.strip()
                if line:  
                    line = line[1:-1]  # Remove square brackets
                    strings = [s.strip().strip("'").strip('"') for s in line.split(',')]
                    data.append(strings)
        return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
def LoadFinding(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

def GenerateTriplesRel1(data_dict):
    result = []
    for key, values in data_dict.items():
        for value in values:
            try:
                # Simulate an error for demonstration
                if CMA(value) == 'string2':  # Example condition to trigger an error
                    raise ValueError(f"Error processing {value}")
                result.append([key, value, CMA(value), 1.0, 'RAG'])
                
            except Exception as e:
                print(f"Error occurred: {e}. Skipping {value}.")
    return result

if __name__ == '__main__':
    
    rag_results = loadRAGResults('rag_result_1.txt')
    findings = LoadFinding('findings.json')
    cases = list(findings.keys())
    mentions = dict(zip(cases, rag_results))
    triples_rel1 = GenerateTriplesRel1(mentions)
    print(mentions)
    print(triples_rel1)