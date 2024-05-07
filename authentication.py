# authentication.py

from OpenSSL import SSL

def verify_callback(connection, cert, errnum, depth, ok):
    # Add custom verification logic here
    return ok

def establish_connection(cert_file, key_file):
    context = SSL.Context(SSL.TLSv1_2_METHOD)
    context.load_cert(cert_file)
    context.load_verify_locations(cafile='ca_cert.pem')
    context.set_verify(SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verify_callback)

    connection = SSL.Connection(context)
    connection.connect(('management_server', 8888))
    return connection
