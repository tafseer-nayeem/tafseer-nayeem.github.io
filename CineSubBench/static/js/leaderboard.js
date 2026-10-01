const table = document.querySelector('#model-leaderboard');

if (table) {
  const headers = [...table.tHead.rows[0].cells];
  const body = table.tBodies[0];
  const viewSwitch = document.querySelector('.view-switch');
  let activeSort = 'composite';
  let descending = true;

  const chart = document.querySelector('#composite-chart');
  if (chart) {
    const list = chart.querySelector('.score-chart-list');
    [...body.rows].sort((a, b) => Number(a.dataset.rank) - Number(b.dataset.rank)).forEach((row) => {
      const score = row.querySelector('.score').textContent.trim();
      const item = document.createElement('li');
      item.className = 'score-chart-row';

      const model = document.createElement('span');
      model.className = 'score-chart-model';
      model.append(row.querySelector('.model-logo').cloneNode(true));
      const name = document.createElement('span');
      name.textContent = row.querySelector('th[scope="row"]').textContent.trim();
      model.append(name);

      const track = document.createElement('span');
      track.className = 'score-chart-track';
      track.setAttribute('aria-hidden', 'true');
      const bar = document.createElement('span');
      bar.className = 'score-chart-bar';
      bar.style.width = `${score}%`;
      track.append(bar);

      const value = document.createElement('strong');
      value.className = 'score-chart-value';
      value.textContent = score;
      item.append(model, track, value);
      list.append(item);
    });
    chart.hidden = false;
  }

  function sortBy(header, direction) {
    const button = header.querySelector('button');
    const sort = button.dataset.sort;
    const column = header.cellIndex;
    activeSort = sort;
    descending = direction;

    const rows = [...body.rows];
    rows.sort((a, b) => {
      const first = sort === 'rank' ? Number(a.dataset.rank) : a.cells[column].textContent.trim();
      const second = sort === 'rank' ? Number(b.dataset.rank) : b.cells[column].textContent.trim();
      const comparison = sort === 'model' || sort === 'family'
        ? first.localeCompare(second)
        : Number(first) - Number(second);
      return (descending ? -comparison : comparison) || Number(a.dataset.rank) - Number(b.dataset.rank);
    });
    body.replaceChildren(...rows);

    headers.forEach((item) => {
      item.removeAttribute('aria-sort');
      item.querySelector('.sort-indicator')?.remove();
    });
    header.setAttribute('aria-sort', descending ? 'descending' : 'ascending');
    const indicator = document.createElement('span');
    indicator.className = 'sort-indicator';
    indicator.setAttribute('aria-hidden', 'true');
    indicator.textContent = descending ? ' \u25bc' : ' \u25b2';
    button.append(indicator);
  }

  headers.forEach((header) => {
    const button = header.querySelector('button');
    button.addEventListener('click', () => {
      const sort = button.dataset.sort;
      const ascendingByDefault = ['rank', 'model', 'family', 'age-mae', 'country-mae'].includes(sort);
      sortBy(header, sort === activeSort ? !descending : !ascendingByDefault);
    });
  });

  viewSwitch.classList.add('is-enabled');
  viewSwitch.querySelectorAll('button').forEach((button) => {
    button.addEventListener('click', () => {
      const view = button.dataset.view;
      table.dataset.view = view;
      table.querySelectorAll('.detail-col').forEach((cell) => { cell.hidden = view !== 'all'; });
      viewSwitch.querySelectorAll('button').forEach((item) => {
        item.setAttribute('aria-pressed', item === button ? 'true' : 'false');
      });
      sortBy(headers.find((header) => header.querySelector('[data-sort="composite"]')), true);
    });
  });
}
