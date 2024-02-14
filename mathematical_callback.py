def process_array(arr, callback):
    return [callback(value) for value in arr]
