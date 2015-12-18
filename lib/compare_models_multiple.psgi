use compare_models_multiple::compare_models_multipleImpl;

use compare_models_multiple::compare_models_multipleServer;
use Plack::Middleware::CrossOrigin;



my @dispatch;

{
    my $obj = compare_models_multiple::compare_models_multipleImpl->new;
    push(@dispatch, 'compare_models_multiple' => $obj);
}


my $server = compare_models_multiple::compare_models_multipleServer->new(instance_dispatch => { @dispatch },
				allow_get => 0,
			       );

my $handler = sub { $server->handle_input(@_) };

$handler = Plack::Middleware::CrossOrigin->wrap( $handler, origins => "*", headers => "*");
