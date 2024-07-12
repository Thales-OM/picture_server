import time
import pickle

class SessionInfoBuffer:
    def __init__(self, buffer_size, ttl, filepath):
        self.buffer_size = int(buffer_size)
        self.ttl = int(ttl)
        self.filepath = str(filepath)
        self.buffer = {}

    def add_session_info(self, session, specific_string, specific_list):
        current_time = time.time()

        # If session exists in buffer, update its data
        if session in self.buffer:
            record = self.buffer[session]
            record['specific_string'] = specific_string
            record['specific_list'] = specific_list
            record['last_updated'] = current_time
            return

        # If buffer is full, write the oldest record to disk
        if len(self.buffer) >= self.buffer_size:
            oldest_session = min(self.buffer, key=lambda x: self.buffer[x]['last_updated'])
            self._write_record_to_disk(self.buffer[oldest_session])

            # Remove oldest record from buffer
            del self.buffer[oldest_session]

        # Add the new session info to buffer
        new_record = {
            'specific_string': specific_string,
            'specific_list': specific_list,
            'last_updated': current_time
        }
        self.buffer[session] = new_record

    def _write_record_to_disk(self, record):
        with open(self.filepath, 'a') as file:
            pickle.dump(record, file)

    def process_expired_records(self):
        current_time = time.time()

        expired_sessions = [session_value for session_value, record in self.buffer.items()
                            if current_time - record['last_updated'] > self.ttl]

        for session_value in expired_sessions:
            self._write_record_to_disk(self.buffer[session_value])
            del self.buffer[session_value]
